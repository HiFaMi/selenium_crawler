from django.contrib import admin

from .models.auth import User

admin.site.register(User)
