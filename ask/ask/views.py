from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def found(request):
    return HttpResponse("Found!")


def not_found(request):
    return HttpResponseNotFound("Not Found!")


