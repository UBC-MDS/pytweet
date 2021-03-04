# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb 2021
import pandas as pd
import altair as alt
from datetime import datetime
import re


# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_tweets(handle, n_tweets=-1):
    """
    Retreives all tweets of a user given their Twitter handle
    (i.e. @elonmusk) through the Twitter API.

    Parameters:
    -----------
    handle : string
        The Twitter handle of the user, or aka the username.
    n_tweets : number
        The total number of tweets you want to retreive from the user.
        By default, n_tweets=-1 means retrieving all tweets. 

    Returns:
    --------
    tweets : dataframe
        A dataframe of the user's tweets, and the sent times.
    """
    
    # TODO
    return None

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