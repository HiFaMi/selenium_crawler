from django.urls import path

from ..views import post_list, post_like, post_like_ajax

app_name = 'posts'
urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:pk>/like/', post_like, name='post-like'),
    path('like/', post_like_ajax, name='post-like-ajax'),

]
