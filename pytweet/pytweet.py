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
        A dataframe contains words that are used, sentiment class, and frenquncy.
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
