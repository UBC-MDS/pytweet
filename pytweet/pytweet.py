# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb 2021

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_tweets(handle):
    """
    Retreives all tweets of a user given their Twitter handle 
    (i.e. @elonmusk) through the Twitter API.

    Parameters:
    -----------
    handle : string
        The Twitter handle of the user, or aka the username.

    Returns:
    --------
    tweets : dataframe
        A dataframe of the user's tweets, and the sent times.
    """

    # TODO
    return None

def plot_timeline(df, time):
    """
    Analysis what time of day the tweets occurs and plot the 
    counts of tweets versus hours. 

    Parameters:
    -----------
    df : dataframe
        A dataframe of the user's tweets, which contains time.

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
    df : dataframe
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
