from django.contrib import admin
from django.urls import path, include
from qa.views import question

urlpatterns = {
    path('<int:pk>/', question),
}