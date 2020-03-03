from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render

from ..forms.profile import ProfileForm


def user_profile(request):

    if request.method == 'POST':

        forms = ProfileForm(request.POST)
        user = request.user
        if forms.is_valid():
            current_password = user.password
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
