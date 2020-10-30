from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    user_str = request.GET['usertext']
    flag = True
    if len(user_str) == 0:
        flag = False
    user_list = user_str.split()
    num = len(user_list)
    length = len(user_str)
    return render(request, 'count.html', {'usertext': user_str, 'length': length, 'num': num, 'flag': flag})
