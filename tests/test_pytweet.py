from pytweet import __version__
from pytweet import pytweet

def test_version():
    assert __version__ == '0.1.0'


def test_get_tweets():
    # test output format
    result = get_tweets('@ShawnMendes')
    assert type(result) == pd.core.frame.DataFrame
    assert columns(result) == ['ID', 'Time', 'Text']
    assert len(result) > 0 # existing user

    # test output status
    assert get_tweets.status == 200

    # test specified n_tweets
    n_tweets = 35
    result = get_tweets('@ShawnMendes', n_tweets=n_tweets)
    assert result.shape[0] == n_tweets

    # test non-existent user
    result = get_tweets('A%@F)UFJSL', n_tweets=20)
    assert len(result) == 0

# def test_get_tweets_error():
