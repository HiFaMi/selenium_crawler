from django.urls import path

from ..api.profile import AuthProfile, AuthProfileGeneric
from ..api.signup import ApiSignUp
from ..api.login import AuthToken, AuthTokenGeneric

app_name = 'members-api'
urlpatterns = [

    path('login/', AuthToken.as_view(), name='api-login'),
    path('login_generic/', AuthTokenGeneric.as_view(), name='api-login-generic'),

    path('signup/', ApiSignUp.as_view(), name='api-signup'),

    path('profile/', AuthProfile.as_view(), name='api-profile'),
    path('profile_generic/', AuthProfileGeneric.as_view(), name='api-profile-generic'),


]
