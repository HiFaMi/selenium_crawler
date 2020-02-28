from django.contrib.auth import login
from django.shortcuts import render, redirect

from members.models.auth import User
from ..forms import UserForm


def signup(request):

    if request.method == 'POST':

        forms = UserForm(request.POST)

        if forms.is_valid():
            new_user = User.objects.create_user(
                username=forms.cleaned_data['username'],
                user_email=forms.cleaned_data['user_email'],
                password=forms.cleaned_data['password']
            )
            login(request, new_user)
            return redirect('post-list')

    else:
        forms = UserForm()

    context = {
        'forms': forms,
    }

    return render(request, 'members/signup.html', context=context)
