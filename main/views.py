from .models import Question
from django.shortcuts import render, get_object_or_404


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


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "main/question_detail.html", {"question": question})
