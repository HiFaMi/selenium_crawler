#!usr/bin/env python

import argparse
import sys

from make_post_class import local_to_twitter_crawler_class, s3_to_facebook_crawler_make_class

MODES = ['local_twitter', 's3_facebook']


def get_mode():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--mode',
        help=f'make class {MODES}'
    )

    args = parser.parse_args()

    mode= args.mode.strip().lower()

    return mode


def mode_function(mode):
    if mode in MODES:
        cur_mode = sys.modules[__name__]
        getattr(cur_mode, f'build_{mode}')()


def build_local_twitter():
    local_to_twitter_crawler_class()


def build_s3_facebook():
    s3_to_facebook_crawler_make_class()


if __name__ == '__main__':
    mode = get_mode()
    mode_function(mode)
