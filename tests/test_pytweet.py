# authors: Huanhuan Li, Yuanzhe(Marco) Ma, Jared Splinter, Yuan Xiong
# date: Feb-Mar 2021

import pandas as pd
from pytweet import __version__
from tweepy import TweepError
from pytweet.pytweet import get_tweets, plot_timeline, plot_hashtags
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
        get_tweets(object('elon'))
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
    tweet_data = pd.read_csv("./tests/trumptweets-test.csv")
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
    with pytest.raises(Exception) as e:
        plot_timeline('', 'date')
        assert str(e.value) == "The value of the argument 'df' " \
                           "must be type of dataframe."
    
    with pytest.raises(Exception) as e:
        plot_timeline(data, 123)
        assert str(e.value) == "The value of the argument 'time_col' must be " \
                           "type of string"

    # Test the plot attributes 
    plot = plot_timeline(data, 'date')
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
    # TODO

    # Test the plot attributes 
    plot = plot_hashtags(data, 'content')
    assert plot.encoding.x.shorthand == 'Count', 'x_axis should be mapped to the x axis'
    assert plot.encoding.y.shorthand == 'Keyword', 'y_axis should be mapped to the y axis'  
    assert plot.mark == 'bar', 'mark should be a bar'

