from django.shortcuts import render
from django.http import HttpResponse
import random

# def generate_pswd():
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     number = '0123456789'
#     special = '!@#$%^&*()_?.'
#     numlist = list(number)
#     alphalist = list(alpha)
#     speciallist = list(special)
#     alphalistUpper = list(alpha.upper())

def generatePswd(request):
    character = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = character.upper()
    character = list('abcdefghijklmnopqrstuvwxyz')
    number = '0123456789'
    special = '!@#$%^&*()_'
    randpswd=""

    num = int(request.GET.get('length'))

    if request.GET.get('upper'):
        character.extend(uppercase)

    if request.GET.get('number'):
        character.extend(number)

    if request.GET.get('special'):
        character.extend(special)

    for i in range(int(num)):
        randpswd += random.choice(character)
    return randpswd

# def printReq(request):
#     upper = request.GET.get('upper')
#     number = request.GET.get('number')
#     special = request.GET.get('special')
#     return [upper, number, special]

def home(request):
    return render(request, 'p_gen_app/home.html')
    # return HttpResponse("Hello world")
    print(request.GET())

def result(request):
    password = generatePswd(request)
    # log = printReq(request)
    return render(request, 'p_gen_app/result.html', {'password':password})
    

