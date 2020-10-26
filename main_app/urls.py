from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
]
