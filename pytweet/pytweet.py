# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb 2021

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
