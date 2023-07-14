
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.signupuser, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
]