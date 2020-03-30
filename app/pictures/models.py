import os

from django.conf import settings
from django.db import models

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

    def delete(self, *args, **kwargs):
        os.remove(f'{MEDIA_ROOT}/{self.post_picture}')
        print(f'{self.post_picture} is deleted')
        super().delete(*args, **kwargs)
