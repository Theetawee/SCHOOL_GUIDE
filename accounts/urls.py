from django.urls import path
from accounts.views import signup_user,logout_user



urlpatterns=[
    path('signup/',signup_user,name='signup'),
    path('logout/',logout_user,name='logout'),
]