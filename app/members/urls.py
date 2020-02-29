from django.urls import path

from .views.auth_logout import user_logout
from .views.auth_login import user_login
from .views.auth_signup import signup

app_name = 'members'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
