from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        user.username = data['username']
        user.user_email = data['email']

        if 'password1' in data:
            user.set_password(data['password1'])

        else:
            user.set_unusable_password()
        self.populate_username(request, user)

        if commit:
            user.save()

        return user
