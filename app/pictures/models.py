import os

import boto3
from django.conf import settings
from django.db import models

from config.settings.base import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from config.settings.dev import MEDIA_ROOT


class PostPicture(models.Model):
    post_user = models.CharField(max_length=150)
    post_modal_target = models.CharField(max_length=100, blank=True)
    post_picture = models.ImageField(upload_to="img")
    post_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like')

    def __str__(self):
        return self.post_modal_target

    @property
    def like_count(self):
        return self.post_likes.count()

    def delete_picture(self, *args, **kwargs):
        session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        s3 = session.client('s3')
        s3.delete_object(Bucket='selenium-crawler', Key=f'.media/{self.post_picture}')
        print(f"{str(self.post_picture).split('/')[-1]} deleted")
        super().delete(*args, **kwargs)
