#!/usr/bin/env python
"""Some youtube-dl niceties"""

from __future__ import unicode_literals, print_function
import argparse
import yaml
import youtube_dl

SERIES_FILE = 'series.yaml'


class MyLogger(object):
    def debug(self, msg):
        if msg.startswith('[download]'):
            print(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def fetch_series():
    """Fetch all series defined in config file"""
    config = yaml.load(open(SERIES_FILE))
    series = config.get('series')
    for url in series.keys():
        fetch_serie(config, url, series.get(url))


def fetch_serie(config, url, opts):
    """Fetch all results for this url"""
    options = config.get('ytdl_opts')
    options['logger'] = MyLogger()
    opts['outtmpl'] = '{}/{}.{}'.format(config.get('target_dir', '.'),
                                        opts.get('outtmpl'), '%(ext)s')
    options.update(opts)
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
