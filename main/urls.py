from django.urls import path,include
from main.views import index , forum

urlpatterns = [
        path('main/',index,name="index"),
        path('forum/',forum,name="forum")
        ]
