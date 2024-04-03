from .models import Question, Subject, Topic
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    title = "StudyGuide - Your Premier E-Learning Platform for Online Tests, Past Papers, Books, and More"
    description = "Explore StudyGuide, your ultimate destination for online tests, past papers, books, and a wealth of educational resources. Enhance your learning experience and excel in your studies with our comprehensive e-learning platform. Start your journey towards academic success today!"
    context = {"title": title, "description": description}

    if "question" in request.GET:
        query = request.GET.get("question")
        results = Question.objects.filter(question_text__icontains=query)
        if request.headers.get("htmx-request"):
            return render(request, "partials/results.html", {"results": results})

    return render(request, "main/index.html", context)


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
    return render(
        request, "main/questions_list.html", {"questions": questions, "topic": topic}
    )


def online_tests(request):
    title = "Online Tests - StudyGuide"
    description = "Take online tests on StudyGuide to assess your knowledge, practice your skills, and prepare for exams. Explore a wide range of subjects and topics with our comprehensive collection of online tests."
    context = {"title": title, "description": description}
    return render(request, "main/online_tests.html", context)
