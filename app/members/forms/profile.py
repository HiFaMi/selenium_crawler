from django import forms
from django.core.exceptions import ValidationError

from ..models.auth import User


class ProfileForm(forms.ModelForm):

    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'new password'}
        )
    )

    new_password_check = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'new password check'}
        )
    )

    class Meta:
        model = User
        fields = (
            'new_password',
            'new_password_check',
        )

    def clean_new_password(self):
        data = self.cleaned_data['new_password']

        if len(data) < 8:
            self.add_error('new_password', "비밀번호는 최소 8글자 이상이여야 합니다.")

        return data

    def clean(self):
        super().clean()
        new_password = self.cleaned_data['new_password']
        check_password = self.cleaned_data['new_password_check']

        if new_password != check_password:
            self.add_error('new_password_check', "두 비밀번호가 같지 않습니다.")

        return self.cleaned_data
