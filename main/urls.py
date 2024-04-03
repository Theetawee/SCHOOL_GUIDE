from django.urls import path
from .views import index, question_detail, subjects


urlpatterns = [
    path("", index, name="home"),
    path("question/<int:pk>", question_detail, name="question_detail"),
    path("subjects/", subjects, name="subjects"),
]
