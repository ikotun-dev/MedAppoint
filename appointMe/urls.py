from django.urls import path
from django.contrib import admin 
from . import views 

urlpatterns =[
    path('', views.index),
    path('home', views.index, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signup', views.signup, name="signup"),
    path('appointment', views.appointment),
    path('contact', views.contact, name="contact")

]