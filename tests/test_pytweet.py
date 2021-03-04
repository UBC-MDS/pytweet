from pytweet import __version__
from pytweet import pytweet

def test_version():
    assert __version__ == '0.1.0'


def test_get_tweets():
    # test output format
    df = get_tweets('@ShawnMendes')
    assert type(df) == 'Pandas Dataframe'
    assert columns(df) == ['ID', 'Time', 'Text']

    # test output status
    assert get_tweets.status == 200

    # test output length
    n_tweets = 35
    df = get_tweets('@ShawnMendes', n_tweets=n_tweets)
    assert df.shape[0] == n_tweets

def test_your:
    df = get_tweets

    df 