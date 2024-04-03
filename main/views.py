from .models import Question, Subject, Topic
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


def subjects(request):
    subjects = Subject.objects.all()
    topics = Topic.objects.all()
    return render(
        request, "main/subjects.html", {"subjects": subjects, "topics": topics}
    )


def questions_list(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
    questions = Question.objects.filter(topic=topic)
    return render(request, "main/questions_list.html", {"questions": questions, "topic": topic})
