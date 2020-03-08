from django.urls import path

from ..api.login import AuthToken

app_name = 'members-api'
urlpatterns = [
    path('login/', AuthToken.as_view(), name='login'),

]
