from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'dfjgklsdfgsdfg'})

def about(request):
    return render(request, 'generator/about.html')    
    
def password(request):
    characters = list('qwertyuioplkjhgfdsazxcvbnm')
    length = int(request.GET.get('length', 12))
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend(list('qwertyuioplkjhgfdsazxcvbnm'.upper()))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for _ in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
