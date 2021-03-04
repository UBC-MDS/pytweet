from pytweet import __version__
#from pytweet import pytweet
from pytweet.pytweet import get_tweets
from pytweet.pytweet import plot_timeline
import pandas as pd
import pytest

def test_version():
    assert __version__ == '0.1.0'

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
    
    # Test the Exception is correctly raised when the type of `df`
    # argument is wrong.
    with pytest.raises(Exception) as e:
        assert plot_timeline('', 'date')
    assert str(e.value) == "The value of the argument 'df' " \
                           "must be type of dataframe."
    
    with pytest.raises(Exception) as e:
        assert plot_timeline(data, 123)
    assert str(e.value) == "The value of the argument 'time_col' must be " \
                           "type of string"

    # Test the plot attributes 
    plot = plot_timeline(data, 'date')
    assert plot.encoding.x.shorthand == 'hour', \
        'The function must return an altair plot' 
    assert plot.encoding.y.shorthand == 'count()', \
        'The function must return an altair plot'   