from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from members.models.auth import User
from ..models import PostPicture


def post_like(request, pk):
    post = get_object_or_404(PostPicture, pk=pk)

    user = User.objects.get(username=request.user)

    if post.post_likes.filter(id=user.id).exists():
        post.post_likes.remove(user)

    else:
        post.post_likes.add(user)

    return HttpResponse(str(post.total_likes()))
