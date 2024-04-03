from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify


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
        return self.title


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField()

    def __str__(self):
        return self.question_text[:50]  # Return first 50 characters of question text


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
