from django.urls import path

from pictures.apis.post_detail import PostDetail
from ..apis.post_like import PostLike
from ..apis.post_list_api import PostList, PostListPagination

app_name = 'posts-api'
urlpatterns = [
    path('list/', PostList.as_view(), name='api-post-list'),
    path('list-pagination/', PostListPagination.as_view(), name='api-post-list-pagination'),

    path('list/<int:pk>/', PostDetail.as_view(), name='api-post-detail'),

    path('list/<int:pk>/like/', PostLike.as_view(), name='api-post-like'),

]
