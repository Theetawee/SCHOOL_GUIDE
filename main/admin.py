from django.contrib import admin
from .models import Topic, Subject, Question, AddOn, Transaction
from django.utils.html import strip_tags


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "get_question_text",
        "topic",
        "paid",
    )
    list_filter = ("topic", "paid")
    search_fields = ("question_text",)

    def get_question_text(self, obj):
        return strip_tags(obj.question_text[:50])

    get_question_text.short_description = "Question"  # Custom column header


admin.site.register(Question, QuestionAdmin)


admin.site.register(Topic)
admin.site.register(Subject)
admin.site.register(AddOn)
admin.site.register(Transaction)
