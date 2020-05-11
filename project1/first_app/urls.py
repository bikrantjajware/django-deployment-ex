
from django.conf.urls import url
from . import  views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

app_name = 'first_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('users/',views.customers,name='customers'),
    path('forms/',views.formpage,name='formpage'),
    path('signup/',views.signup,name='signuppage'),
    path('login/',views.login,name='login'),
]