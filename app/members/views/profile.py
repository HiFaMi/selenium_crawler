from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from ..forms.profile import ProfileForm


def user_profile(request):

    if request.method == 'POST':

        forms = ProfileForm(request.POST)
        user = request.user
        if forms.is_valid():
            current_password = user.password
            new_password = forms.cleaned_data['new_password']
            if check_password(current_password, forms.cleaned_data['new_password']):
                forms.add_error(forms.cleaned_data['new_password'], "기존의 비밀번호는 사용하실 수 없습니다.")

            else:
                user.set_password(forms.cleaned_data['new_password'])
                return redirect('posts:post-list')

    else:
        forms = ProfileForm()

    context = {
        'forms': forms,
    }

    return render(request, 'members/profile.html', context=context)


def django_profile(request):

    if request.method == 'POST':
        user = request.user
        forms = PasswordChangeForm(user=user, data=request.POST)

        if forms.is_valid():
            changed_user = forms.save()
            update_session_auth_hash(request, changed_user)
            messages.success(request, "변경에 성공하셨습니다.")
            return redirect('posts:post-list')
        else:
            messages.error(request, "다시 시도해주시기 바랍니다.")

    forms = PasswordChangeForm(request.POST)

    context = {
        'forms': forms
    }

    return render(request, 'members/django-profile.html', context=context)


def user_like(request):
    user = request.user

    user_likes_list = user.like.all()

    context = {
        'posts': user_likes_list,
    }

    return render(request, 'members/like_post.html', context=context)
