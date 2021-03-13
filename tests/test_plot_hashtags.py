import pandas as pd
from pytweet.pytweet import plot_hashtags
from pytest import raises


def test_plot_hashtags():
    """
    Tests the hashtags function to make sure the outputs are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    data = pd.read_csv("tests/brunomars_data.csv")

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
