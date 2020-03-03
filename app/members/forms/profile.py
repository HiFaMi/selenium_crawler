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

    def clean(self):
        super().clean()
        new_password = self.cleaned_data['new_password']
        check_password = self.cleaned_data['new_password_check']

        if new_password != check_password:
            self.add_error(new_password, "두 비밀번호가 같지 않습니다.")
            self.add_error(check_password, "두 비밀번호가 같지 않습니다.")
