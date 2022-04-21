from asyncio import constants
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User

from django.http import HttpResponse
# current active user


def profile(request, username=None):

    if(User.objects.get(username=username)):
        user = User.objects.get(username=username)
        return render(request, 'profile.html', {'user': user})
    else:
        return render(request, 'profile.html')


def detail(request, question_id):
    return HttpResponse("new Page" + str(question_id))


def post(request):
    return render(request, 'post.html')


def after_logged(request):
    return render(request, 'index1.html')


def login(request):
    return render(request, 'login.html')
