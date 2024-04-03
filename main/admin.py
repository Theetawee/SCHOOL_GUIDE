from django.contrib import admin
from .models import Topic, Subject, Question, AddOn

# Register your models here.


admin.site.register(Topic)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(AddOn)
