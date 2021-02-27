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


def sentiment_analysis (tweets):
    """
    This function first trains a Logistic Regression model based on the Natural Languange Processing (NLP) Kit and use this model to do a sentiment study on the given tweets (input).

    Parameters:
    -----------
    tweets : dataframe
        A dataframe of the user's tweets, and the sent times.

    Returns:
    --------
    tweets_senti : dataframe
        A dataframe contains words that are used, sentiment class, and frenquncy. 
    """
    # TODO
    return None


def sentiment_plot (tweets_senti):
        """
    This function creats a wordcloud plot based on the tweets_senti data (input).

    Parameters:
    -----------
    tweets_senti : dataframe
        A dataframe contains words that are used, sentiment class, and frenquncy. 

    Returns:
    --------
    senti_plots : plot
        Three plots of wordcloud that correponds to all tweets, tweets with positive sentiment and tweets with negative sentiment.
    """
    # TODO
    return None