from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from ..models import PostPicture


def post_list(request):
    posts_list = PostPicture.objects.all()

    # show 21 contacts per page
    paginator = Paginator(posts_list, 21)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }

    return render(request, 'posts/post_list.html', context)
