from django.urls import path

from ..api.signup import ApiSignUp
from ..api.login import AuthToken

app_name = 'members-api'
urlpatterns = [
    path('login/', AuthToken.as_view(), name='login'),
    path('signup/', ApiSignUp.as_view(), name='signup'),

]
