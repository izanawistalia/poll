from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('detail/<str:pk>/', views.detail, name="detail"),
    path('vote/<str:pk>/', views.vote, name="vote"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('logoutPage', views.logoutPage, name="logoutPage"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('create/', views.create, name="create"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
]
