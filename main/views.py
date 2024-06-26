from .models import Question, Subject, Topic, AddOn, Transaction
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.html import strip_tags
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from base.settings.base import APP_NAME
from django.core.mail import send_mail
from .forms import EmailForm


# Create your views here.
def index(request):
    title = f"{APP_NAME} - Your Premier E-Learning Platform for Online Tests, Past Papers, Books, and More"
    description = f"Explore {APP_NAME}, your ultimate destination for online tests, past papers, books, and a wealth of educational resources. Enhance your learning experience and excel in your studies with our comprehensive e-learning platform. Start your journey towards academic success today!"
    context = {"title": title, "description": description}

    # Get the query parameter
    query = request.GET.get("question")

    if query:
        # Filter the questions based on the query
        all_results = Question.objects.filter(
            Q(topic__title__icontains=query)
            | Q(question_text__icontains=query)
            | Q(topic__subject__name__icontains=query)
        )

        # Paginate the results
        paginator = Paginator(all_results, 5)
        page_number = request.GET.get("page")
        try:
            results = paginator.page(page_number)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        # Check if it's an HTMX request
        if request.htmx:
            return render(
                request,
                "partials/results.html",
                {"results": results, "total": paginator.count},
            )

        else:
            context["total"] = paginator.count
            context["results"] = results
            return render(request, "main/index.html", context)

    return render(request, "main/index.html", context)


@login_required
def question_detail(request, pk):
    page_name = "Question"
    # reffer
    # reffer = request.META.get("HTTP_REFERER")
    question = get_object_or_404(Question, pk=pk)
    if request.user.subscribed is False:
        messages.warning(
            request, "You don't have enough points to access this question."
        )
        return redirect("payments")
    add_ons = AddOn.objects.filter(question=question)
    title = (
        strip_tags(f"{question.question_text[:50]}... - {APP_NAME}")
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("&nbsp;", " ")
    )
    description = (
        strip_tags(
            f"Explore the details of the question: '{question.question_text}'. Test your knowledge and understanding with {APP_NAME}."
        )
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("&nbsp;", " ")
    )
    context = {
        "title": title,
        "description": description,
        "question": question,
        "add_ons": add_ons,
        "page_name": page_name,
    }
    return render(request, "main/question_detail.html", context)


def subjects(request):
    title = f"Subjects - {APP_NAME}"
    description = f"Explore a wide range of subjects and topics on {APP_NAME}. Dive into various fields of study, including mathematics, science, history, and more. Access comprehensive resources and enhance your learning experience."
    page_name = "Subjects"
    subjects = Subject.objects.all()
    topics = Topic.objects.all()
    context = {
        "title": title,
        "description": description,
        "subjects": subjects,
        "topics": topics,
        "page_name": page_name,
    }
    return render(request, "main/subjects.html", context)


def questions_list(request, topic_slug):
    page_name = "Questions"
    topic = get_object_or_404(Topic, slug=topic_slug)
    title = f"{topic.title} - {APP_NAME}"
    description = f"Explore questions related to {topic.title} on {APP_NAME}. Test your knowledge and understanding of {topic.title} with our comprehensive collection of questions."
    questions = Question.objects.filter(topic=topic)

    # Pagination
    paginator = Paginator(questions, 5)
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    context = {
        "title": title,
        "description": description,
        "questions": questions,
        "topic": topic,
        "page_name": page_name,
        "total": paginator.count,
    }
    return render(request, "main/questions_list.html", context)


def online_tests(request):
    title = f"Online Tests - {APP_NAME}"
    description = f"Take online tests on {APP_NAME} to assess your knowledge, practice your skills, and prepare for exams. Explore a wide range of subjects and topics with our comprehensive collection of online tests."
    context = {"title": title, "description": description}
    return render(request, "main/online_tests.html", context)


def books_list(request):
    title = f"Books - {APP_NAME}"
    description = f"Explore a vast collection of educational books on {APP_NAME}. Find textbooks, reference materials, and study guides to enhance your learning experience and excel in your studies."
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


@login_required
def remove_addon(request, pk):

    addon = get_object_or_404(AddOn, pk=pk)
    question = addon.question
    addon.delete()
    add_ons = AddOn.objects.filter(question=question)
    return render(
        request, "partials/add_ons.html", {"add_ons": add_ons, "question": question}
    )


@login_required
def payments_details(request):
    context = {}
    page_name = "Payments"
    title = f"Payments - {APP_NAME}"
    description = f"Payment details on {APP_NAME}."
    context["page_name"] = page_name
    context["title"] = title
    context["description"] = description
    if request.method == "POST":
        transaction_id = request.POST.get("transaction_id")
        if transaction_id:
            new_transaction_id = int(transaction_id)
            transaction = Transaction.objects.filter(transation_id=new_transaction_id)
            if transaction.exists():
                request.user.last_paid = timezone.now()
                request.user.save()
                transaction.update(used=True, use_date=timezone.now())
                messages.success(
                    request, "Your payment was successful. You are now a subscriber."
                )
                return redirect("payments")
            else:
                messages.error(
                    request,
                    "Can't process your payment. Please try again after some time.",
                )
                return redirect("payments")
    return render(request, "main/payments.html", context)


@login_required
def email_user(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            recipients = form.cleaned_data["recipients"]

            # Loop through the recipients and send individual emails
            for recipient in recipients:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=request.user.email,  # Use the email of the logged-in user as the sender
                    recipient_list=[
                        recipient.email
                    ],  # Send email to each recipient separately
                    fail_silently=False,
                )
            messages.success(request, "Emails sent successfully!")
            return redirect("email_user")
    else:
        form = EmailForm()
    return render(request, "main/email.html", {"form": form})


def about_us(request):
    title = f"About Us - {APP_NAME} "
    description = f"Learn more about {APP_NAME} - your premier destination for online learning. Discover our mission, vision, and commitment to providing high-quality educational resources."
    page_name = "About"

    context = {"title": title, "description": description, "page_name": page_name}

    return render(request, "main/about.html", context)
