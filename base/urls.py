from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('register/', views.registerUser,name="register"),
    path('',views.home, name="home"),
    path('room/<str:pk>/', views.room , name="room"),
    path('profile/<str:pk>/', views.profile , name="user-profile"),
    path('create-room/', views.createRoom ,name="create_room"),
    path('update-room/<str:pk>/', views.updateRoom ,name="update_room"),
    path('delete-room/<str:pk>/', views.deleteRoom ,name="delete_room"),
    path('delete-message/<str:pk>/', views.deleteMessage ,name="delete_message"),
    
    
    path('update-user/', views.updateUser ,name="update-user")
]
