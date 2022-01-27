from django.urls import path,include
from main.views import index , forum,questionPost,search,particularPost

urlpatterns = [
        path('',index,name="index"),
        path('forum/',forum,name="forum"),
        path('posts/',questionPost,name="posts"),
        path('search/',search,name="search"),
        path('posts/<int:id>',particularPost,name="particularPost")

        ]
