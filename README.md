# pytweet 

![](https://github.com/mmyz88/pytweet/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/mmyz88/pytweet/branch/main/graph/badge.svg)](https://codecov.io/gh/mmyz88/pytweet) ![Release](https://github.com/mmyz88/pytweet/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pytweet/badge/?version=latest)](https://pytweet.readthedocs.io/en/latest/?badge=latest)

## Package Overview           
`pytweet` is a python package for text analysis and sentiment analysis on tweets. The package will allow you to extract tweets from Twitter, visualize user habit on tweet posting, and apply sentiment analysis to the data.        

## Features

- `get_tweets`:              
    - This function extracts tweets from a Twitter user given their handle (i.e. @elonmusk). 

- `plot_timeline`:             
    - This function creates an analysis of what time of day the tweets occurs and plots the counts of tweets and hours. 

- `plot_hashtags`:             
    - This function creates an analysis of the hashtags in tweets, and plots the most frequently used hashtag words.

- `tweet_sentiment_analysis`:              
    - This function applies sentiment analysis to tweets. It associates tokens in tweets with positive or negative sentiments and calculates their corresponding frequencies.           

- `visualize_sentiment`:            
    -    This function takes in the output of sentiment_analysis function and creates a visualization of user's tweets with sentimental analysis.
## Related Packages           
There are a few existing Python packages that perform tweets text analysis and sentiment analysis available on PyPI, such as [tweet-scraper](https://pypi.org/project/tweet-scraper/), and [tweet-sentiment](https://pypi.org/project/tweet-sentiment/). Also, there are similar packages available on Github, such as [twitter_sentiment_analysis](https://github.com/namas191297/twitter_sentiment_analysis). However, there are no available packages for hashtag or timeline visualization. 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pytweet
```

## Dependencies

- python = "^3.8"
- pandas = "^1.2.3"
- altair = "^4.1.0"
- DateTime = "^4.3"
- tweepy = "^3.10.0"
- textblob = "^0.15.3"
- sklearn = "^0.0"
- nltk = "3.5"
- strings = "0.1.2"

## Usage
```Python
import pytweet
import pandas as pd

pytweet.get_tweets('@BrunoMars', n_tweets=8)
```
```
>                   time                                              tweet
> 0  2021-03-06 04:39:46              ✨✨✨✨✨✨✨✨✨✨✨✨✨ https://t.co/ElGgeZ7B9c
> 1  2021-03-05 20:41:06  ✨ #SilkSonic #LeaveTheDoorOpen @AndersonPaak @...
> 2  2021-03-05 20:31:45                                                  👀
> 3  2021-03-05 05:18:36  ✨ #SilkSonic song and video out now✨ #LeaveThe...
> 4  2021-03-05 03:14:22                                         #SilkSonic
> 5  2021-03-03 20:48:20        Just posted a photo https://t.co/wPsxKeCAWH
> 6  2021-03-02 19:32:41  Lacoste: “Bruno, if you want the clothes to se...
> 7  2021-03-02 16:03:35  Alright i’ll be back. I gotta go approve some ...
```

```Python
tweet_data = pytweet.get_tweets('@BrunoMars', n_tweets=500)
pytweet.plot_timeline(tweet_data, 'time')
```
<img src="https://raw.githubusercontent.com/UBC-MDS/pytweet/main/img/timeline_plot.png" width="500">

```Python
pytweet.plot_hashtags(tweet_data, 'tweet')
```
<img src="https://raw.githubusercontent.com/UBC-MDS/pytweet/main/img/hashtag_plot.png" width="500">

```Python
tweet_sentiment_analysis(tweet_data)
```
<img src="https://raw.githubusercontent.com/UBC-MDS/pytweet/main/img/sentiment_analysis_example.png" width="800">

```Python
Sentiment_df = pytweet.tweet_sentiment_analysis(tweet_data)
visualize_sentiment(Sentiment_df)
```
<img src="https://raw.githubusercontent.com/UBC-MDS/pytweet/main/img/visualize_sentiment_plot.png" width="700">

## Documentation

The official documentation is hosted on Read the Docs: https://pytweet.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/mmyz88/pytweet/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
