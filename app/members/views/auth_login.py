from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post-list')
        else:
            return redirect('members:login')

    else:
        return render(request, 'members/login.html')

