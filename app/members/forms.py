from django import forms
from django.core.exceptions import ValidationError

from .models.auth import User


class UserForm(forms.ModelForm):

    password_check = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Password Check'},
        ),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'user_email',
            'password',
            'password_check',
        )

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ID'}),
            'user_email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password'}),
        }

    def clean_username(self):

        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError("이미 사용중인 아이디 입니다.")
        return data

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']

        if password != password_check:
            self.add_error("비밀번호와 비밀번호 확인 값이 일치하지 않습니다.")

        return self.cleaned_data
