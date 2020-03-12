#!/usr/bin/env python

import argparse
import os
import subprocess
import sys

MODES = ['base', 'dev', 'production']


def get_mode():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--mode',
        help='Docker build mode {}'.format(MODES),
    )

    args = parser.parse_args()

    if args.mode:
        mode = args.mode.strip().lower()

    else:
        while True:
            for index, mode_name in enumerate(MODES, start=1):
                print('{} : {}'.format(index, mode_name))

            select_mode = input('Choice: ')

            try:
                mode_index = int(select_mode) -1
                mode = MODES[mode_index]
                break
            except IndexError:
                print("1~{}번을 입력하세요".format(len(MODES)))

    return mode


def mode_function(mode):
    if mode in MODES:
        cur_mode = sys.modules[__name__]
        getattr(cur_mode, 'build_{}'.format(mode))()

    else:
        raise ValueError("{}에 속하는 값만 가능합니다.".format(MODES))


def build_base():
    subprocess.call('docker build -t crawler:base -f Dockerfile.base .', shell=True)


def build_dev():
    try:
        subprocess.call('poetry export -f requirements.txt --dev > requirements.txt', shell=True)
        subprocess.call('docker build -t crawler:dev -f Dockerfile.dev .', shell=True)
    finally:
        os.remove('requirements.txt')


def build_production():
    try:
        subprocess.call('poetry export -f requirements.txt > requirements.txt', shell=True)
        subprocess.call('docker build -t crawler:production -f Dockerfile.production .', shell=True)
    finally:
        os.remove('requirements.txt')


if __name__ == '__main__':
    mode = get_mode()
    mode_function(mode)




