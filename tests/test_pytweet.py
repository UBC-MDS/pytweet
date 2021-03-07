# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb-Mar 2021

import pandas as pd
from pytweet import __version__
from tweepy import TweepError
from pytweet.pytweet import *
from pytest import raises
# import pytest
import re

def test_version():
    assert __version__ == '0.1.0'

def test_get_tweets():
    """
    Test existing functionalities of get_tweets(), which include
    returning a dataframe in the right format, the n_tweets argument
    and the include_replies argument.

    6 tests in total.
    """
    result = get_tweets('@ShawnMendes')

    # test output type
    assert type(result) == pd.core.frame.DataFrame

    # test output column names
    assert sum(result.columns == ['time', 'tweet'])  # True if both are true

    # test output dataframe size (for an existing user)
    assert len(result) > 0

    # test n_tweets argument
    n = 35
    result = get_tweets('@ShawnMendes', n_tweets=n)
    assert result.shape[0] == n

    # test include_replies argument, defult = False
    result = get_tweets('@ShawnMendes')
    result_rp = get_tweets('@ShawnMendes', include_replies=True)
    assert len(result_rp) > len(result)


def test_get_tweets_error():
    """
    Test error cases and error messages thrown by get_tweets.

    5 tests in total.
    """
    # test invalid handle
    with raises(TypeError) as e:
        get_tweets(123)
    assert str(e.value) == 'Invalid argument type: handle must be a string.'

    # test invalid n_tweets
    with raises(TypeError) as e:
        get_tweets('elonmusk', n_tweets='football')
    assert str(e.value) == 'Invalid argument: input n_tweets must be >= 0.'

    # test invalid include_replies
    with raises(TypeError) as e:
        get_tweets('elonmusk', include_replies=3)
    assert str(e.value) == 'Invalid argument type: include_replies must be boolean.'

    # test invalid verbose
    with raises(TypeError) as e:
        get_tweets('elonmusk', verbose='nah')
    assert str(e.value) == 'Invalid argument type: verbose must be boolean.'

    # test non-existent user
    with raises(TweepError):
        result = get_tweets('A%@F)UFJSL', n_tweets=20)

        
def helper_create_data():
    """
    Helper function for creating dataframe for testing
    Parameters
    -----------
    Returns
    --------
    pandas.DataFrame
        Returns a dataframe to be used for testing
    Examples
    ---------
    >>> helper_create_data()
    """
    tweet_data = pd.read_csv("./tests/brunomars_data.csv")
    return tweet_data

def test_plot_timeline():
    """
    Tests the plot_timeline function to make sure the outputs are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    data = helper_create_data()
    
    # Test the Exception is correctly raised when the type of 
    # arguments are wrong
    with raises(Exception) as e:
        plot_timeline('', 'time')
    assert str(e.value) == "The value of the argument 'df' " \
                           "must be type of dataframe."
    
    with raises(Exception) as e:
        plot_timeline(data, 123)
    assert str(e.value) == "The value of the argument 'time_col' must be " \
                           "type of string"

    # Test the plot attributes 
    plot = plot_timeline(data, 'time')
    assert plot.encoding.x.shorthand == 'hour', 'x_axis should be mapped to the x axis'
    assert plot.encoding.y.shorthand == 'count()', 'y_axis should be mapped to the y axis'  
    assert plot.mark == 'line', 'mark should be a line'
    
def test_plot_hashtags():
    """
    Tests the hashtags function to make sure the outputs are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    data = helper_create_data()

    # Test the Exception is correctly raised when the type of 
    # arguments are wrong
    with raises(Exception) as e:
        plot_hashtags('', 'tweet')
    assert str(e.value) == "The value of the argument 'df' " \
                           "must be type of dataframe."
    
    with raises(Exception) as e:
        plot_hashtags(data, 123)
    assert str(e.value) == "The value of the argument 'text_col' must be " \
                           "type of string"

    # Test the plot attributes 
    plot = plot_hashtags(data, 'tweet')
    assert plot.encoding.x.shorthand == 'Count', 'x_axis should be mapped to the x axis'
    assert plot.encoding.y.shorthand == 'Keyword', 'y_axis should be mapped to the y axis'  
    assert plot.mark == 'bar', 'mark should be a bar'

def test_tweet_sentiment_analysis():
    """
    Test existing functionalities of tweet_sentiment_analysis(), which supposed to be a dataframe with semetiment results
    """
    data = helper_create_data()
    result = tweet_sentiment_analysis('data')

    # make sure the input is a dataframe
    assert type(result) == pd.core.frame.DataFrame 
  
    # make sure the output has the correct columns 
    assert sum(result.columns == ['time', 'tweet', 'polarity', 'sentiment', 'neg', 'neu', 'pos', 'compound']) 
    
    # make sure the output is not empty. 
    assert len(result) > 0

def test_tweet_sentiment_analysis_error():
    """
    Test error cases and error messages thrown by tweet_sentiment_analysis.
    3 tests in total.
    """
    # test invalid input
    with raises(TypeError) as e:
        tweet_sentiment_analysis('@ShawnMendes')
    assert str(e.value) == 'Invalid argument type: input must be a dataframe.'


def test_visualize_sentiments():
    """
    Tests the visualize_sentiments function to make sure the outputs are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    data = helper_create_data()
    data2 = helper_create_data()
    # Run sentiment analysis
    sentiment = tweet_sentiment_analysis(data)
    
    #Error Checks
    with raises(TypeError) as e:
        visualize_sentiment(sentiment, "single")
    assert str(e.value) == "Invalid argument for plot_type: You must enter one of 'Standard', 'Stacked', 'Separate'"

    with raises(Exception) as e:
        visualize_sentiment("data")
    assert str(e.value) == "The input of sentiment_df should be a Pandas DataFrame, did you use output of tweet_sentiment_analysis?"

    with raises(KeyError) as e:
        visualize_sentiment(data2)
    assert str(e.value) == "'Input does not contain column for sentiment, did you use output of tweet_sentiment_analysis?'"
        
    #standard bar chart checks
    standard_plot = visualize_sentiment(sentiment)
    assert str(type(standard_plot)) == "<class 'altair.vegalite.v4.api.Chart'>"
    assert standard_plot.encoding.x.shorthand == 'frequency','x_axis should be mapped to the x_axis'
    assert standard_plot.encoding.y.shorthand == 'Word', 'y_axis should be mapped to the y_axis'
    assert standard_plot.mark == 'bar'
    
    #concatonated bar chart check
    separate_plot = visualize_sentiment(sentiment,"Separate")
    assert str(type(separate_plot)) == "<class 'altair.vegalite.v4.api.HConcatChart'>"