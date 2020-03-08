from django.urls import path
from ..apis.post_list_api import PostList, PostListPagination

app_name = 'posts-api'
urlpatterns = [
    path('list/', PostList.as_view(), name='post-list'),
    path('list-pagination/', PostListPagination.as_view(), name='post-list-pagination'),

]
