from django.urls import path

from .views.auth import signup

urlpatterns = [
    path('signup/', signup, name='sign-up')

]
