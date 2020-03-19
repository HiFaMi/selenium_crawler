#!/usr/bin/env python

import json
import os
import subprocess
import argparse
import sys

MODES = ['kill_crawler', 'kill_selenium', 'deploy', 'base', 'maker', 'oneclick', 'selenium']

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, '.secret')

secrets = json.load(open(os.path.join(SECRET_DIR, 'secrets.json')))


AWS_KEY_ROOT = secrets['AWS']['AWS_ACCESS_KEY_ROOT']
AWS_URL_CONNECT = secrets['AWS']['AWS_URL_CONNECT']
ROOT_PASSWORD = secrets['ROOT']['PASSWORD']

AWS_CONNECT = 'ssh -i {} {}'.format(AWS_KEY_ROOT, AWS_URL_CONNECT)
AWS_SCP_FILE = 'scp -i {}'.format(AWS_KEY_ROOT)


def get_mode():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--mode',
        help="AWS deploy mode {}".format(MODES)
    )

    args = parser.parse_args()

    mode = args.mode.strip().lower()

    return mode


def mode_function(mode):
    if mode in MODES:
        cur_mode = sys.modules[__name__]
        getattr(cur_mode, 'build_{}'.format(mode))()

    else:
        raise ValueError('{} 안에 있는 값만 가능합니다.'.format(MODES))


def build_kill_crawler():
    command = subprocess.check_output("{} sudo docker ps --filter ancestor=crawler:production -q".format(AWS_CONNECT), shell=True)
    if bool(command) is True:
        print("crawler:production docker process is activated\nkill docker process")
        subprocess.call("{} sudo docker stop {}".format(AWS_CONNECT, command.decode('utf-8')[:-2]), shell=True)
        print("kill")
    else:
        print("None docker process")


def build_kill_selenium():
    command = subprocess.check_output("{} sudo docker ps --filter ancestor=selenium:run -q".format(AWS_CONNECT), shell=True)
    if bool(command) is True:
        print("selenium:run docker process is activated\nkill docker process")
        subprocess.call("{} sudo docker stop {}".format(AWS_CONNECT, command.decode('utf-8')[:-2]), shell=True)
        print("kill")
    else:
        print("None docker process")


def build_deploy():
    subprocess.call("{} sudo docker build -t crawler:production -f /home/ubuntu/project/Dockerfile.production /home/ubuntu/project/.".format(AWS_CONNECT), shell=True)
    subprocess.call("{} sudo docker run -d -p 80:80 crawler:production".format(AWS_CONNECT), shell=True)
    print('Running Dockerfile')


def build_base():

    subprocess.call("{} sudo docker build -t crawler:base -f /home/ubuntu/project/Dockerfile.base /home/ubuntu/project/.".format(AWS_CONNECT), shell=True)
    print("Base build")


def build_maker():
    try:
        subprocess.call('poetry export -f requirements.txt > requirements.txt', shell=True)
        subprocess.call("{} sudo rm -rf project".format(AWS_CONNECT), shell=True)
        subprocess.call("echo {} | sudo -S {} -r ~/project/poetry_test/ {}:".format(ROOT_PASSWORD, AWS_SCP_FILE, AWS_URL_CONNECT), shell=True)
        subprocess.call("{} sudo mv /home/ubuntu/poetry_test /home/ubuntu/project".format(AWS_CONNECT), shell=True)
        print('Rename to project')

    finally:
        os.remove('requirements.txt')


def build_selenium():
    build_kill_selenium()
    subprocess.call("{} sudo docker build -t selenium:base -f /home/ubuntu/project/Dockerfile.selenium_base /home/ubuntu/project/.".format(AWS_CONNECT), shell=True)
    subprocess.call("{} sudo docker build -t selenium:run -f /home/ubuntu/project/Dockerfile.selenium /home/ubuntu/project/.".format(AWS_CONNECT), shell=True)
    subprocess.call("{} sudo docker run -d --rm -it selenium:run".format(AWS_CONNECT), shell=True)


def build_oneclick():
    build_kill_crawler()
    build_maker()
    build_deploy()


if __name__ == '__main__':
    mode = get_mode()
    mode_function(mode)



