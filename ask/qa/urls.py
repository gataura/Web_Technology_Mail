from django.conf.urls import url

from ask.qa.views import test

urlpatterns = [
    url('(?<num>\d+)/', test),
]