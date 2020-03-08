from django.urls import path

from ..views.profile import user_profile, django_profile, user_like
from ..views.auth_logout import user_logout
from ..views.auth_login import user_login
from ..views.auth_signup import signup

app_name = 'members'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),

    path('profile_test/', django_profile, name='django-profile'),

    path('like-post/', user_like, name='user-like'),
]
