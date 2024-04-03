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
        if request.htmx:
            return render(request, "partials/results.html", {"results": results})

    return render(request, "main/index.html", context)


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    title = f"{question.topic} - {question.question_text[:50]}..."
    description = f"Explore the details of the question: '{question.question_text}'. Test your knowledge and understanding with StudyGuide."
    context = {"title": title, "description": description, "question": question}
    return render(request, "main/question_detail.html", context)


def subjects(request):
    title = "Subjects - StudyGuide"
    description = "Explore a wide range of subjects and topics on StudyGuide. Dive into various fields of study, including mathematics, science, history, and more. Access comprehensive resources and enhance your learning experience."
    subjects = Subject.objects.all()
    topics = Topic.objects.all()
    context = {
        "title": title,
        "description": description,
        "subjects": subjects,
        "topics": topics,
    }
    return render(request, "main/subjects.html", context)


def questions_list(request, topic_slug):
    topic = get_object_or_404(Topic, slug=topic_slug)
    title = f"{topic.title} - StudyGuide"
    description = f"Explore questions related to {topic.title} on StudyGuide. Test your knowledge and understanding of {topic.title} with our comprehensive collection of questions."
    questions = Question.objects.filter(topic=topic)
    context = {
        "title": title,
        "description": description,
        "questions": questions,
        "topic": topic,
    }
    return render(request, "main/questions_list.html", context)


def online_tests(request):
    title = "Online Tests - StudyGuide"
    description = "Take online tests on StudyGuide to assess your knowledge, practice your skills, and prepare for exams. Explore a wide range of subjects and topics with our comprehensive collection of online tests."
    context = {"title": title, "description": description}
    return render(request, "main/online_tests.html", context)


def books_list(request):
    title = "Books - StudyGuide"
    description = "Explore a vast collection of educational books on StudyGuide. Find textbooks, reference materials, and study guides to enhance your learning experience and excel in your studies."
    context = {"title": title, "description": description}
    return render(request, "main/books.html", context)
