from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasks),
    path('register/',views.register),
    path('signin/',views.signin),
    path('signout/',views.signout)
]