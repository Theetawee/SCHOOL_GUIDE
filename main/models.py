from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from accounts.models import Account


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    @property
    def number_of_topics(self):
        return self.topic_set.count()

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=100)

    def __str__(self):
        return f"{self.title} - {self.subject.name}"


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = CKEditor5Field("Text", config_name="extends")
    answer_text = CKEditor5Field("Text", config_name="extends")
    likes = models.ManyToManyField(Account, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(Account, related_name="dislikes", blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text[:50]  # Return first 50 characters of question text


class AddOn(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account.username

    class Meta:
        ordering = ["-pub_date"]


class Transaction(models.Model):
    transation_id = models.PositiveIntegerField()
    used = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    use_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.transation_id)


@receiver(post_save, sender=Subject)
def create_subject_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()


@receiver(post_save, sender=Topic)
def create_topic_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()
