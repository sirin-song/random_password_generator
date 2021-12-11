from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse('Hello there... friend')
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    characters_uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    characters_special = list('!@#$%^&*()_+')
    characters_numbers = list('1234567890')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(characters_uppercase)

    if request.GET.get('special'):
        characters.extend(characters_special)

    if request.GET.get('numbers'):
        characters.extend(characters_numbers)

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')