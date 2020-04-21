from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    SOCIAL_CHOICES = (
        ('L', 'local'),
        ('K', 'kakao'),
        ('D', 'discord'),
        ('GG', 'google'),
        ('GH', 'github'),
    )

    username = models.CharField(max_length=50, unique=True)
    user_email = models.EmailField(verbose_name="이메일")
    social = models.CharField(max_length=2, choices=SOCIAL_CHOICES, default='L')
    order = models.PositiveIntegerField(null=True)
