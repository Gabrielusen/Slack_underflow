from django.shortcuts import render
from django.http import HttpResponse
# from django.conf import settings


# User = settings.AUTH_USER_MODEL


def index(request):
    return render(request, 'index.html')
