from .models import Question, Subject, Topic, AddOn
from django.shortcuts import redirect, render, get_object_or_404


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
    add_ons = AddOn.objects.filter(question=question)
    title = f"{question.topic} - {question.question_text[:50]}..."
    description = f"Explore the details of the question: '{question.question_text}'. Test your knowledge and understanding with StudyGuide."
    context = {
        "title": title,
        "description": description,
        "question": question,
        "add_ons": add_ons,
    }
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


def like_question(request, pk):
    if not request.user.is_authenticated:
        return render(request, "partials/status/not-allowed.html")
    question = get_object_or_404(Question, pk=pk)

    if request.user in question.likes.all():
        # Remove the user from likes if they have previously liked the question
        question.likes.remove(request.user)

        return render(
            request, "partials/status/nolike-nodislike.html", {"question": question}
        )

    if request.user in question.dislikes.all():
        # Remove the user from dislikes if they have previously disliked the question
        question.dislikes.remove(request.user)

    # Add the user to the likes list
    question.likes.add(request.user)

    # Redirect the user to the question detail page
    return render(
        request, "partials/status/like-nodislike.html", {"question": question}
    )


def dislike_question(request, pk):
    if not request.user.is_authenticated:
        return render(request, "partials/status/not-allowed.html")
    question = get_object_or_404(Question, pk=pk)

    if request.user in question.dislikes.all():
        # Remove the user from likes if they have previously liked the question
        question.dislikes.remove(request.user)

        return render(
            request, "partials/status/nolike-nodislike.html", {"question": question}
        )

    if request.user in question.likes.all():
        # Remove the user from dislikes if they have previously disliked the question
        question.likes.remove(request.user)

    # Add the user to the likes list
    question.dislikes.add(request.user)

    # Redirect the user to the question detail page
    return render(
        request, "partials/status/nolike-dislike.html", {"question": question}
    )


def question_addon(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.POST:
        comment = request.POST.get("comment")
        new_addon = AddOn.objects.create(
            question=question, account=request.user, comment=comment
        )
        new_addon.save()
        add_ons = AddOn.objects.filter(question=question)
        return render(
            request, "partials/add_ons.html", {"add_ons": add_ons, "question": question}
        )
    return redirect("question_detail", pk=question.pk)
