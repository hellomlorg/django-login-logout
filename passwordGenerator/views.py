from django.shortcuts import render
import pyperclip
import random


# Create your views here.
def passhome(request):
    return render(request, 'passwordGenerator/passhome.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list(r'!@#$%^&*<>?-_:'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    pyperclip.copy(thepassword)
    return render(request, 'passwordGenerator/password.html', {'password': thepassword})
