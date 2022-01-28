from django.contrib import admin
from .models import Question, QuestionComment
# Register your models here.
@admin.register(Question, QuestionComment)
class AppAdmin(admin.ModelAdmin):
    pass
