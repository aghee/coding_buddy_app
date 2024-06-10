from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('userprofile/<str:pk>',views.userProfile,name="userprofile"),
    path('room/<str:pk>',views.oneroom,name="oneroom"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room"),
    path('delete-msg/<str:pk>/',views.deleteMessage,name="delete-msg"),
    path('edit-msg/<str:pk>/',views.editMessage,name="edit-msg"),
]
