from django.urls import path
from .views import (
    index,
    question_detail,
    subjects,
    questions_list,
    online_tests,
    books_list,
)


urlpatterns = [
    path("", index, name="home"),
    path("question/<int:pk>", question_detail, name="question_detail"),
    path("subjects/", subjects, name="subjects"),
    path("questions/<slug:topic_slug>/", questions_list, name="questions_list"),
    path("online-tests/", online_tests, name="online_tests"),
    path("books/", books_list, name="books"),
]
