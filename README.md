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
    - This function creates an analysis of the hashtags in tweets, and plots the hashtag analysis.

- `sentiment_analysis`:              
    - This function applies sentiment analysis to tweets. It associates tokens in tweets with positive or negative sentiments and calculates their corresponding frequencies.           

- `visualize_sentiment`:            
    -    This function takes in the output of sentiment_analysis function and creates a visualization of user's tweets with sentimental analysis.
## Related Packages           
There are a few existing Python packages that perform tweets text analysis and sentiment analysis available on PyPI, such as [tweet-scraper](https://pypi.org/project/tweet-scraper/), and [tweet-sentiment](https://pypi.org/project/tweet-sentiment/). Also, there are similar packages available on Github, such as [twitter_sentiment_analysis](https://github.com/namas191297/twitter_sentiment_analysis). However, there are no available packages for hashtag or emoji visualization. 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pytweet
```

## Dependencies

- TODO

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://pytweet.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/mmyz88/pytweet/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
