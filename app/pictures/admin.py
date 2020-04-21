from django.contrib import admin

from .models import PostPicture


class PostPicturesAdmin(admin.ModelAdmin):
    list_display = ['post_user', 'post_picture', 'like_count']
    list_display_links = ['post_picture']


admin.site.register(PostPicture, PostPicturesAdmin)
