from django.shortcuts import render

from ..models import PostPicture


def post_list(request):
    posts = PostPicture.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'posts/post_list.html', context)
