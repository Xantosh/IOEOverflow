from django.urls import path,include
from main.views import index , forum,questionPost,search

urlpatterns = [
        path('main/',index,name="index"),
        path('forum/',forum,name="forum"),
        path('posts/',questionPost,name="posts"),
        path('search/',search,name="search")

        ]
