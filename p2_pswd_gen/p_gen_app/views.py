from django.shortcuts import render
from django.http import HttpResponse
import random

def generate_pswd():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    special = '!@#$%^&*()_?.'
    numlist = list(number)
    alphalist = list(alpha)
    speciallist = list(special)
    alphalistUpper = list(alpha.upper())

def generateRand(request):
    character = 'abcdefghijklmnopqrstuvwxyz'
    randpswd=""
    num = int(request.GET.get('length'))
    for i in range(int(num)):
        randpswd += random.choice(character)
    return randpswd

def printReq(request):
    upper = request.GET.get('upper')
    number = request.GET.get('number')
    special = request.GET.get('special')
    return [upper, number, special]

def home(request):
    return render(request, 'p_gen_app/home.html')
    # return HttpResponse("Hello world")
    print(request.GET())

def result(request):
    password = generateRand(request)
    log = printReq(request)
    return render(request, 'p_gen_app/result.html', {'password': password, 'log' : log})
    

