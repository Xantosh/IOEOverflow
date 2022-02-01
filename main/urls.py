from django.urls import path,include
from main.views import index , forum,questionPost,search,particularPost,registerUser,loginUser,logoutUser,upvote_increment,downvote_increment,freshStart

urlpatterns = [
        path('',index,name="index"),
        path('forum/',forum,name="forum"),
        path('posts/',questionPost,name="posts"),
        path('search/',search,name="search"),
        path('posts/<int:id>',particularPost,name="particularPost"),
        path('register',registerUser,name="register"),
        path('login',loginUser,name="login"),
        path('logout',logoutUser,name="logout"),
        path('upvote/<int:id>',upvote_increment,name="upvote"),
        path('downvote/<int:id>',downvote_increment,name="downvote"),
        path('fresh',freshStart,name="freshStart")

        ]
