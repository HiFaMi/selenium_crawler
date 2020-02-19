from django.db import models


class PostPicture(models.Model):
    post_user = models.CharField(max_length=150)
    post_picture = models.ImageField(upload_to="images")
