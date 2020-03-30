#!/usr/bin/env python

import os

import boto3
import django
django.setup()

from config.settings.base import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from pictures.models import PostPicture

PRESENT_DIR = os.path.abspath('')
IMG_DIR = os.path.join(PRESENT_DIR, '.media/img')
FACEBOOK_DIR = os.path.join(PRESENT_DIR, '.media/img/facebook')


def local_to_twitter_crawler_class():
    dir_lists = os.listdir(IMG_DIR)
    for dir_list in dir_lists:
        if os.path.isdir(os.path.join(IMG_DIR, dir_list)):
            class_user_name = dir_list
            img_lists = os.listdir(os.path.join(IMG_DIR, dir_list))
            new_img_counter = 0
            for img_list in img_lists:
                if PostPicture.objects.filter(post_picture='img/{}/{}'.format(class_user_name, img_list)).exists() is False:
                    post = PostPicture.objects.create(
                        post_user=class_user_name,
                        post_picture='img/{}/{}'.format(class_user_name, img_list)
                    )
                    post.save()

                    post = PostPicture.objects.last()
                    post.post_modal_target = "PostModalTarget{}".format(post.id)
                    post.save()

                    new_img_counter += 1

            if new_img_counter == 0:
                print("nothing new img about {}".format(dir_list))
            else:
                print("new img about {}: +{}".format(dir_list, new_img_counter))
    print("Done")


def local_to_facebook_crawler_make_class():

    img_lists = os.listdir(FACEBOOK_DIR)
    new_img_counter = 0
    for img_list in img_lists:
        if PostPicture.objects.filter(post_picture=f'img/facebook/{img_list}').exists() is False:
            PostPicture.objects.create(
                post_user='facebook',
                post_picture=f'img/facebook/{img_list}'
            )
            post = PostPicture.objects.last()
            post.post_modal_target = "PostModalTarget{}".format(post.id)
            post.save()

            new_img_counter += 1

    if new_img_counter == 0:
        print("nothing new img about facebook")
    else:
        print(f"new img about facebook: +{new_img_counter}")
    print("Done")


def s3_to_facebook_crawler_make_class():
    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3 = session.resource('s3')
    bucket = s3.Bucket('selenium-crawler')

    new_post = 0

    for obj in bucket.objects.filter(Delimiter='/', Prefix='.media/img/facebook/'):
        path = obj.key.split('/')[-1]

        if path:
            if not PostPicture.objects.filter(post_picture=f'img/facebook/{path}').exists():
                PostPicture.objects.create(
                    post_user='facebook',
                    post_picture=f'img/facebook/{path}'
                )
                post = PostPicture.objects.last()
                post.post_modal_target = post.id
                post.save()

                new_post += 1

    print(f'create {new_post} new post class')


if __name__ == '__main__':
    local_to_facebook_crawler_make_class()