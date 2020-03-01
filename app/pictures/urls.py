from django.urls import path

from .views import post_list, post_like

app_name = 'posts'
urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:pk>/like', post_like, name='post-like'),

]
