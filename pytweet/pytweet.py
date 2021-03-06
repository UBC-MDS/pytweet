# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb-Mar 2021

import tweepy
import os
import pandas as pd
import altair as alt
import re
from datetime import datetime
from tweepy import TweepError
from textblob import TextBlob
import numpy as np
import nltk
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')

def get_tweets(handle, n_tweets=-1, include_replies=False, verbose=True):
    """
    Retreives all tweets of a user given their Twitter handle
    (i.e. @elonmusk) through Twitter API. User must have API 
    keys and secrets stored as os environment variables.

    Parts of the function references Brown University CSCI0931's
    lecture notes: https://cs.brown.edu/courses/csci0931/2015-fall/3-synthesis/LEC3-5.pdf

    Parameters:
    -----------
    handle : string
        The Twitter handle of the user, aka the username.
    n_tweets : number
        The total number of tweets to retreive. Must be positive.
        By default, n_tweets=-1 retrieves all tweets.
    include_replies : boolean
        Whether or not to downloaded the users replies
        in addition to original tweets/retweets.
    verbose : boolean
        Whether or not to print out the progress during the fetch.

    Returns:
    --------
    tweets : dataframe
        A dataframe of the user's tweets, and the sent times.
    """

    # check argument validity
    if not(isinstance(handle, str)):
        raise TypeError('Invalid argument type: handle must be a string.')
    elif not(isinstance(n_tweets, int) and n_tweets >= -1):
        raise TypeError('Invalid argument: input n_tweets must be >= 0.')
    elif not(isinstance(include_replies, bool)):
        raise TypeError('Invalid argument type: include_replies must be boolean.')
    elif not(isinstance(verbose, bool)):
        raise TypeError('Invalid argument type: verbose must be boolean.')

    # Twitter API credentials
    try:
        consumer_key = os.environ.get('TWITTER_CONS_KEY')
        consumer_secret = os.environ.get('TWITTER_CONS_SEC')
        access_key = os.environ.get('TWITTER_ACCS_KEY')
        access_secret = os.environ.get('TWITTER_ACCS_SEC')
    except KeyError:
        raise Exception('Need authentication tokens! Please make sure you have those as environment variables.')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # get first batch of tweets
    tweets = []
    latest = api.user_timeline(screen_name=handle,
                               exclude_replies=not(include_replies),
                               count=200)  # max count per request is 200
    
    tweets.extend(latest)

    # request recursively to get all tweets/n_tweets
    oldest = latest[-1].id
    while(len(latest) > 0 and len(tweets) < n_tweets):
        latest = api.user_timeline(screen_name=handle, 
                                   exclude_replies=not(include_replies), 
                                   count=200, max_id=oldest)
        tweets.extend(latest)
        oldest = latest[-1].id

        if verbose:
            print(f"{len(tweets)} tweets downloaded")

    # format output dataframe
    output = pd.DataFrame([[tweet.created_at, tweet.text] for tweet in tweets],
                          columns=['time', 'tweet'])
    if n_tweets != -1:
        output = output[:n_tweets]

    return output


def plot_timeline(df, time_col):
    """
    Analysis what time of day the tweets occurs and plot the
    counts of tweets versus hours. 

    Parameters:
    -----------
    tweets : dataframe
        A dataframe of the user's tweets, and the sent times.
    time: string
        The column name of post time in dataframe.

    Returns:
    --------
    plot: chart
        A chart plotting the counts of tweets versus hours.
    """

    # Checking for valid inputs
    if not isinstance(df, pd.DataFrame):
        raise Exception("The value of the argument 'df' must be " \
                        "type of dataframe.")
    if type(time_col) != str:
        raise Exception("The value of the argument 'time_col' must be " \
                        "type of string")
    
    # extract hour from time column
    df['time'] = df[time_col].apply(lambda x: datetime.strptime(x, "%m/%d/%Y %H:%M"))
    df['hour'] = df['time'].apply(lambda x: x.hour)
    
    # timeline plot
    timeline_plot = alt.Chart(df).mark_line().encode(
        x=alt.X('hour', title = "Hour of day"),
        y=alt.Y('count()',title = "Counts of Tweets")).properties(title='Tweet Timeline Analysis')
    return timeline_plot


def plot_hashtags(df, text_col):
    """
    Analysis the hashtags in tweets, and plot the hashtag
    analysis.

    Parameters:
    -----------
    tweets : dataframe
        A dataframe of the user's tweets.

    tweet: string
        The column name of tweet text in dataframe.

    Returns:
    --------
    plot: chart
        A chart plotting analysis result of using hashtags.
    """
    
    #extract hashtags from text
    df['hashtags'] = df[text_col].apply(lambda x: re.findall(r'[#] \w+', x))
    
    # count hashtags
    hashtag_dict = {}
    for hashtags in df["hashtags"]:
        for word in hashtags:
            hashtag_dict[word] = hashtag_dict.get(word, 0) + 1

    hashtag_df = pd.DataFrame(columns = ['Keyword', 'Count'])
    for key, value in hashtag_dict.items():
        key_value = [[key, value]]
        hashtag_df = hashtag_df.append(pd.DataFrame(key_value, columns=['Keyword', 'Count']),\
                                       ignore_index=True)
    
    # hashtag frequency plot
    hashtag_plot = alt.Chart(hashtag_df).mark_bar().encode(
        x=alt.X('Count', title = "Hashtags"),
        y=alt.Y('Keyword',title = "Count of Hashtags",
                 sort = '-x')
        ).properties(title='Top 15 Hashtag Analysis'
        ).transform_window(rank='rank(Count)',
                           sort=[alt.SortField('Count', order='descending')]
        ).transform_filter((alt.datum.rank <= 15)
    )
    return hashtag_plot

def tweet_sentiment_analysis(tweets):
    """
    This function examine and categorize each tweet in the dataframe into either 'positive' or 'negative' or neutral' sentiments. 
    The sentiment information together with the related scores are added to the original dataframe.

    Parameters:
    -----------
    tweets : dataframe
        A dataframe of the user's tweets, and the sent times.

    Returns:
    --------
    tweets_senti : dataframe
        A new dataframe that has added 'sentiment' category and related score informations onto the input dataframe. 
    """
    tweets_senti = tweets
    tweets_senti[['polarity', 'subjectivity']] = tweets_senti['tweet'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
    for index, row in tweets_senti['tweet'].iteritems():
        score = SentimentIntensityAnalyzer().polarity_scores(row)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        if neg > pos:
            tweets_senti.loc[index, 'sentiment'] = 'negative'
        elif pos > neg:
            tweets_senti.loc[index, 'sentiment'] = 'positive'
        else:
            tweets_senti.loc[index, 'sentiment'] = 'neutral'
        tweets_senti.loc[index, 'neg'] = neg
        tweets_senti.loc[index, 'neu'] = neu
        tweets_senti.loc[index, 'pos'] = pos
        tweets_senti.loc[index, 'compound'] = comp
        
    return tweets_senti

def text_cleaning(text):
    """
    This helper function cleans the tweet text. The cleaning process includes:  remove puntuation, tokenization, 
    remove stopwords and stemming. This helper function will be called in the tweet_rank function to facilitate tween ranking analysis.

    Parameters:
    -----------
    text : np.array
        A np.array that contains a list of strings (tweets). 

    Returns:
    --------
    text : np.array
        A np.array that contains a list of strings (cleaned tweets) 
    """
    stopword = nltk.corpus.stopwords.words('english')
    stopword.append('')
    stopword.append('cont')
    ps = SnowballStemmer('english')
    text_lc = "".join([word.lower() for word in text if word not in string.punctuation]) # remove puntuation
    text_rc = re.sub('[0-9]+', '', text_lc)
    tokens = re.split('\W+', text_rc)    # tokenization
    text = [ps.stem(word) for word in tokens if word not in stopword]  # remove stopwords and stemming
    return text 

def visualize_sentiment(sentiment_df, plot_type = "Standard"):
    """
    Takes in the output of sentiment_analysis and creates
    a visualization of user's tweets with sentimental analysis.

    Parameters:
    -----------
    sentiment_df : dataframe
        Output of tweet_sentiment_analysis,
        dataframe that contains added columns from tweet_sentiment_analysis
    
    plot_type : string
        Optional: Type of plot to return, 3 options:'Standard', 'Stacked', and 'Separate'
        'Standard' Returns bar plot of most common words tweeted color coded by sentiment
        'Stacked' Returns same as 'Standard' but if words are found in other sentiments they are stacked together
        'Separate' Returns 3 bar plots with the sentiment of 'Postive' 'Neutral', and 'Negative' separated

    Returns:
    --------
     plot:
        A bar plot of the user's tweets containing in order
        the most common words, colour coded by the word's sentiment class.
    """
    
    #check inputs
    options = ("Standard", "Stacked", "Separate")
    if plot_type not in options:
        raise TypeError("Invalid argument for plot_type: You must enter one of 'Standard', 'Stacked', 'Separate'")
    elif not isinstance(sentiment_df, pd.DataFrame):
        raise Exception("The input of sentiment_df should be a Pandas DataFrame, did you use ouput of tweet_sentiment_analysis?")
    elif 'sentiment' not in sentiment_df:
        raise KeyError("Input does not contain column for sentiment, did you use ouput of tweet_sentiment_analysis?")

    #Define tweet_rank function
    def tweet_rank (df, sentiment):
        """function to return most common words tweeted for a specified sentiment"""
        df_senti = df[df['sentiment']==sentiment]
        countVectorizer = CountVectorizer(analyzer=text_cleaning, stop_words = 'english') 
        countVector = countVectorizer.fit_transform(df_senti['tweet'])
        count_vect_df = pd.DataFrame(countVector.toarray(), columns=countVectorizer.get_feature_names())
        count_vect_df.head()
        count = pd.DataFrame(count_vect_df.sum())
        countdf = count.sort_values(0,ascending=False).head(20)
        return countdf[1:11]
    
    
    dataframes = dict()            #create empty dictionary to store sentiment dataframes
    for sentiment in np.unique(sentiment_df["sentiment"]):
        sent_df = tweet_rank(sentiment_df, sentiment)
        sent_df.columns = ['frequency']                #rename columns and include column for sentiment and word
        sent_df["sentiment"] = sentiment
        sent_df['Word'] = sent_df.index
        dataframes[sentiment] = sent_df     #append sentiment dataframe to dictionary

    top_words_df = pd.concat([dataframes['positive'], dataframes['neutral'], dataframes['negative']]) #add all dataframes together, may need adjustment later

    #Plot if standard is selected
    if plot_type == "Standard":
        top_words_df['Word'] = top_words_df['Word'] + ' ('+ top_words_df["sentiment"] +')'
        standard_plot = alt.Chart(top_words_df, title='Most Common Words used by Twitter User').mark_bar().encode(
                            x=alt.X('frequency', title= 'Number of Occurences'),
                            y=alt.Y('Word', sort = '-x'),
                            color=alt.Color("sentiment", scale=alt.Scale(domain = ['positive', 'neutral', 'negative'], range=['blue', 'orange', 'red'])))
        return standard_plot
    
   #Plot if stacked is selected
    elif plot_type == "Stacked":
        top_words_df['Word'] = top_words_df.index
        stacked_plot =  alt.Chart(top_words_df, title='Most Common Words used by Twitter User').mark_bar().encode(
                            x=alt.X('frequency', title= 'Number of Occurences'),
                            y=alt.Y('Word', sort = '-x'),
                            color=alt.Color("sentiment", scale=alt.Scale(domain = ['positive', 'neutral', 'negative'], range=['blue', 'orange', 'red'])))
        return stacked_plot
    
    #Plot if Separate is selected
    elif plot_type == "Separate":
        negative = alt.Chart(dataframes['negative'], title='Most Common Negative Words used by Twitter User').mark_bar().encode(
            x=alt.X('frequency', title= 'Number of Occurences'),
            y=alt.Y('Word', sort = '-x'),
            color=alt.value("red"))

        positive = alt.Chart(dataframes['positive'], title='Most Common Postive Words used by Twitter User').mark_bar().encode(
            x=alt.X('frequency', title= 'Number of Occurences'),
            y=alt.Y('Word', sort = '-x'),
            color=alt.value("blue"))

        neutral = alt.Chart(dataframes['neutral'], title='Most Common Neutral Words used by Twitter User').mark_bar().encode(
            x=alt.X('frequency', title= 'Number of Occurences'),
            y=alt.Y('Word', sort = '-x'),
            color=alt.value("orange"))
        
        separate_plot = positive | neutral | negative
        return separate_plot


## for generate toydata
#output = get_tweets('@pytweetGod')
#output.to_csv("../tests/toy_data.csv")

## for generate plots
#import altair_saver
#tweet_data = pd.read_csv("../tests/trumptweets-test.csv")
#timeline = plot_timeline(tweet_data, 'time')
#timeline.save('../img/timeline_plot.html')
#hashtags = plot_hashtags(tweet_data, 'tweet')
#hashtags.save('../img/hashtag_plot.html')
