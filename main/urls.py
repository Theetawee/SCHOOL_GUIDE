from django.urls import path
from .views import (
    index,
    question_detail,
    subjects,
    questions_list,
    online_tests,
    books_list,
    like_question,
    dislike_question,
    question_addon,
    remove_addon
)


urlpatterns = [
    path("", index, name="home"),
    path("question/<int:pk>", question_detail, name="question_detail"),
    path("subjects/", subjects, name="subjects"),
    path("questions/<slug:topic_slug>/", questions_list, name="questions_list"),
    path("online-tests/", online_tests, name="online_tests"),
    path("books/", books_list, name="books"),
    path("like-question/<int:pk>/", like_question, name="like-question"),
    path("dislike-question/<int:pk>/", dislike_question, name="dislike-question"),
    path("question-addon/<int:pk>/", question_addon, name="question_addon"),
    path("remove-addon/<int:pk>/", remove_addon, name="remove_addon"),
]
