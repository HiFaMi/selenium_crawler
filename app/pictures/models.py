from django.db import models


class PostPicture(models.Model):
    post_user = models.CharField(max_length=150)
    post_modal_target = models.CharField(max_length=100, blank=True)
    post_picture = models.ImageField(upload_to="img")
