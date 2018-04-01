from django.contrib import admin
from django.urls import path, include
from qa.views import test

urlpatterns = {
    path('<int:pk>', test),
}