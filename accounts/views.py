from django.shortcuts import render


def user_account(request):
    title = "Account - StudyGuide"
    description = "Explore a vast collection of educational books on StudyGuide. Find textbooks, reference materials, and study guides to enhance your learning experience and excel in your studies."
    return render(request, "main/account.html", {"title": title, "description": description})
