# import pandas as pd
from pytweet.pytweet import plot_timeline, get_tweets
from pytest import raises


def test_plot_timeline():
    """
    Tests the plot_timeline function to make sure the outputs are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    # data = pd.read_csv("tests/brunomars_data.csv")
    data = get_tweets('@BrunoMars', n_tweets=200)

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
