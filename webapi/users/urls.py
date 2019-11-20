from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserList),
    path('user/<int:pk>/', views.UserDetail),
]