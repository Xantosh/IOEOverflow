from django.urls import path,include
from main.views import index , forum,questionPost

urlpatterns = [
        path('main/',index,name="index"),
        path('forum/',forum,name="forum"),
        path('posts/',questionPost,name="posts")

        ]
