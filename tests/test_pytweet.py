from pytweet import __version__
import pandas as pd
from pytweet.pytweet import get_tweets
from pytest import raises
# import pytest

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
    with raises(Exception):
        result = get_tweets('A%@F)UFJSL', n_tweets=20)
        assert str(e.value) == 'User does not exist.'
