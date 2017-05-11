#!/usr/bin/env python
"""Some youtube-dl niceties"""

from __future__ import unicode_literals
import argparse
import yaml
import youtube_dl

SERIES_FILE = 'series.yaml'

# Global options
# https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L133
OPTS = {
    'nooverwrites': True,
    'writesubtitles': True,
    'subtitleslangs': ['en', 'no'],
}


def fetch_series():
    """Fetch all series defined in config file"""
    config = yaml.load(open(SERIES_FILE))
    series = config.get('series')
    for url in series.keys():
        fetch_serie(config.get('target_dir', '.'), url, series.get(url))


def fetch_serie(target_dir, url, opts):
    """Fetch all results for this url"""
    options = OPTS.copy()
    opts['outtmpl'] = '{}/{}.{}'.format(target_dir, opts.get('outtmpl'), '%(ext)s')
    options.update(opts)
    print "Saving to %s" % opts['outtmpl']
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])


def fetch_info(url):
    """Fetch the json file containing meta-information"""
    options = {
        'skip_download': True,
        'writeinfojson': True,
        'playlist_items': "1",
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='url', help='Fetch information about url')
    return parser


if __name__ == '__main__':
    args = create_parser().parse_args()
    if args.url:
        fetch_info(args.url)
    else:
        fetch_series()
