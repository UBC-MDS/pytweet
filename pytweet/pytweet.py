# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb-Mar 2021

import tweepy
import os
import pandas as pd
import altair as alt
import re
from datetime import datetime
from tweepy import TweepError

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
    df['time'] = df[time_col].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
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
        A chart plotting analysis result of most frequent used hashtag words.
    """
    # Checking for valid inputs
    if not isinstance(df, pd.DataFrame):
        raise Exception("The value of the argument 'df' must be " \
                        "type of dataframe.")
    if type(text_col) != str:
        raise Exception("The value of the argument 'text_col' must be " \
                        "type of string")
    
    #extract hashtags from text
    df['hashtags'] = df[text_col].apply(lambda x: re.findall(r'[#]\w+', x))
    
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
        ).properties(title='Top 15 Hashtag Words'
        ).transform_window(rank='rank(Count)',
                           sort=[alt.SortField('Count', order='descending')]
        ).transform_filter((alt.datum.rank <= 15)
    )
    return hashtag_plot

def sentiment_analysis(tweets):
    """
    This function first trains a Logistic Regression model based on the Natural Languange Processing (NLP) Kit
    and use this model to do a sentiment study on the given tweets (input).

    Parameters:
    -----------
    tweets : dataframe
        A dataframe of the user's tweets, and the sent times.

    Returns:
    --------
    tweets_df : dataframe
        A dataframe contains words that are used, sentiment class, and frequency.
    """

    # TODO
    return None

def visualize_sentiment(sentiment_df):
    """
    Takes in the output of sentiment_analysis and creates
    a visualization of user's tweets with sentimental analysis.

    Parameters:
    -----------
    sentiment_df : dataframe
        Output of sentimenet_analysis,
        dataframe that contains columns for words, sentiment class, and frequency

    Returns:
    --------
     plot:
        A bar plot of the user's tweets containing in order
        the most common words, colour coded by the word's sentiment class.
    """

    # TODO
    return None

## for generate toydata
#output = get_tweets('@BrunoMars', n_tweets=500)
#output.to_csv("../tests/brunomars_data.csv")

## for generate plots
#import altair_saver
#tweet_data = pd.read_csv("../tests/brunomars_data.csv")
#timeline = plot_timeline(tweet_data, 'time')
#timeline.save('../img/timeline_plot.html')
#hashtags = plot_hashtags(tweet_data, 'tweet')
#hashtags.save('../img/hashtag_plot.html')