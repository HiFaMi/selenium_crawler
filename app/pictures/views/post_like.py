import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from members.models.auth import User
from ..models import PostPicture


def post_like(request, pk):
    post = get_object_or_404(PostPicture, pk=pk)

    user = User.objects.get(username=request.user)

    if post.post_likes.filter(id=user.id).exists():
        post.post_likes.remove(user)

    else:
        post.post_likes.add(user)

    return redirect('posts:post-list')


@login_required
@require_POST
def post_like_ajax(request):
    pk = request.POST.get('pk', )
    post = get_object_or_404(PostPicture, pk=pk)
    user = User.objects.get(pk=request.user.id)

    if post.post_likes.all().filter(pk=user.id):
        post.post_likes.remove(user)

    else:
        post.post_likes.add(user)

    context = {
        'like_count': post.like_count,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")
