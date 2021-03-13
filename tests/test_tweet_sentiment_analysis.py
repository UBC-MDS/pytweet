import pandas as pd
from pytweet.pytweet import tweet_sentiment_analysis, get_tweets
from pytest import raises


def test_tweet_sentiment_analysis():
    """
    Test existing functionalities of tweet_sentiment_analysis(),
    which supposed to be a dataframe with semetiment results
    """
    # data = pd.read_csv("tests/brunomars_data.csv")
    data = get_tweets('@BrunoMars', n_tweets=200)
    data = data[["time", "tweet"]]
    result = tweet_sentiment_analysis(data)

    # make sure the input is a dataframe
    assert type(result) == pd.core.frame.DataFrame

    # make sure the output has the correct columns
    assert sum(result.columns == ['time', 'tweet', 'polarity', 'subjectivity',
                                  'sentiment', 'neg', 'neu', 'pos', 'compound'])

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
