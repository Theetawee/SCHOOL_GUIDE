from django.shortcuts import render
from base.settings.base import APP_NAME


def user_account(request):
    page_name = "Account"
    title = f"Account - {APP_NAME}"
    description = f"Explore a vast collection of educational books on {APP_NAME}. Find textbooks, reference materials, and study guides to enhance your learning experience and excel in your studies."
    return render(
        request,
        "main/account.html",
        {"title": title, "description": description, "page_name": page_name},
    )
