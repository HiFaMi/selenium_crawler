from django.urls import path

from ..api.change_password import ChangePassword
from ..api.delete import AuthDelete
from ..api.logout import AuthLogout
from ..api.profile import AuthProfile, AuthProfileGeneric
from ..api.signup import ApiSignUp, SignUpGeneric
from ..api.login import AuthToken, AuthTokenGeneric

app_name = 'members-api'
urlpatterns = [

    path('login/', AuthToken.as_view(), name='api-login'),
    path('login_generic/', AuthTokenGeneric.as_view(), name='api-login-generic'),

    path('logout/', AuthLogout.as_view(), name='api-logout'),

    path('signup/', ApiSignUp.as_view(), name='api-signup'),
    path('signup_generic/', SignUpGeneric.as_view(), name='api-signup-generic'),

    path('profile/', AuthProfile.as_view(), name='api-profile'),
    path('profile_generic/', AuthProfileGeneric.as_view(), name='api-profile-generic'),

    path('delete/', AuthDelete.as_view(), name='api-delete'),

    path('change_password/', ChangePassword.as_view(), name='api-change-password'),

]
