# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb 2021

import tweepy
from tweepy import TweepError
import os
import pandas as pd

def get_tweets(handle, n_tweets=-1, include_replies=False, verbose=True):
    """
    Retreives all tweets of a user given their Twitter handle
    (i.e. @elonmusk) through Twitter API.

    User must have Twitter API tokens and secrets stored as os
    environment variables.

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
    try:
        latest = api.user_timeline(screen_name=handle,
                                   exclude_replies=not(include_replies),
                                   count=200)  # max count per request is 200
    except TweepError:
        raise Exception('User does not exist.')
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


def plot_timeline(df, time):
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

    # TODO
    return None

def plot_hashtags(df, tweet):
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

    # TODO
    return None

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
