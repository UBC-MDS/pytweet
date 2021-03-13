import pandas as pd
from pytweet.pytweet import tweet_sentiment_analysis, visualize_sentiment
from pytest import raises


def test_visualize_sentiments():
    """
    Tests the visualize_sentiments function to make sure the outputs are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Get test dataset
    data = pd.read_csv("tests/brunomars_data.csv")
    data2 = pd.read_csv("tests/brunomars_data.csv")

    # Run sentiment analysis
    sentiment = tweet_sentiment_analysis(data)

    # Error Checks
    with raises(TypeError) as e:
        visualize_sentiment(sentiment, "single")
    assert str(e.value) == "Invalid argument for plot_type: You must enter one of 'Standard', 'Stacked', 'Separate'"

    with raises(Exception) as e:
        visualize_sentiment("data")
    assert str(e.value) == """The input of sentiment_df should be a Pandas DataFrame,
                           did you use output of tweet_sentiment_analysis?"""

    with raises(KeyError) as e:
        visualize_sentiment(data2)
    assert str(e.value) == "'Input does not contain column for sentiment," \
                           " did you use output of tweet_sentiment_analysis?'"

    # standard bar chart checks
    standard_plot = visualize_sentiment(sentiment)
    assert str(type(standard_plot)) == "<class 'altair.vegalite.v4.api.Chart'>"
    assert standard_plot.encoding.x.shorthand == 'frequency', 'x_axis should be mapped to the x_axis'
    assert standard_plot.encoding.y.shorthand == 'Word', 'y_axis should be mapped to the y_axis'
    assert standard_plot.mark == 'bar'

    # concatonated bar chart check
    separate_plot = visualize_sentiment(sentiment, "Separate")
    assert str(type(separate_plot)) == "<class 'altair.vegalite.v4.api.HConcatChart'>"
