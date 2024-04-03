from .models import Question
from django.shortcuts import render


# Create your views here.
def index(request):
    if "question" in request.GET:
        query = request.GET.get("question")
        results = Question.objects.filter(question_text__icontains=query)
        if request.htmx:
            return render(request, "partials/results.html", {"results": results})
    else:
        results = Question.objects.none()
    return render(request, "main/index.html", {"results": results})
