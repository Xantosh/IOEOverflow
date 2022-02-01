from django.contrib import admin
from .models import Question, QuestionComment,TotalEntries
# Register your models here.
@admin.register(Question, QuestionComment,TotalEntries)

class AppAdmin(admin.ModelAdmin):
    pass
