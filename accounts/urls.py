from .views import user_account
from django.urls import path

urlpatterns = [
    path("me/", user_account, name="user"),
]
