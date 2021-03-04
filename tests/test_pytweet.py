from pytweet import __version__
import pandas as pd
from pytweet.pytweet import get_tweets
# import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_get_tweets():
    """
    Test existing functionalities of get_tweets(), which include
    returning a dataframe in the right format, the n_tweets argument
    and the include_replies argument.

    7 tests in total. 
    """
    # test output format
    result = get_tweets('@ShawnMendes')
    assert type(result) == pd.core.frame.DataFrame
    assert sum(result.columns == ['time', 'tweet'])  # True if all three are true
    assert len(result) > 0  # existing user

    # test n_tweets argument
    n_tweets = 35
    result = get_tweets('@ShawnMendes', n_tweets=n_tweets)
    assert result.shape[0] == n_tweets

    # test include_replies argument, defult = False
    result = get_tweets('@ShawnMendes')
    result_rp = get_tweets('@ShawnMendes', include_replies=True)
    assert len(result_rp) > len(result)

    # test non-existent user
    result = get_tweets('A%@F)UFJSL', n_tweets=20)
    assert len(result) == 0

def test_get_tweets_error():
    
