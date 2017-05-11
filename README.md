# My youtube download helper

## Make it work

Use virtualenv for requirements:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

When running:

    source venv/bin/activate
    ./ytd.py

## Config

First line is url to youtube-dl. The rest is config to it. See [available options for youtube-dl](https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L133)
