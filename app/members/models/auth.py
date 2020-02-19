from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField(max_length=50)
    user_email = models.EmailField(verbose_name="이메일")
