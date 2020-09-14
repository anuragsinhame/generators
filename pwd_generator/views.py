from django.shortcuts import render
# Custom imports
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def pwd_generator(request):
    # if (request.GET['get_password']=="GetPassword"):
        password    =   ""
        characters  =   list("123CGFV@#$cfhf")
        length      =   int(request.GET.get('pwd_length',12))
        lowercase   =   'abcdefghijklmnopqrstuvwxyz'
        uppercase   =   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers     =   '0123456789'
        special     =   '!@#$%&*()'
        if(request.GET.get('lowercase')):
            characters.extend(list(lowercase))
        if(request.GET.get('uppercase')):
            characters.extend(list(uppercase))
        if(request.GET.get('numbers')):
            characters.extend(list(numbers))
        if(request.GET.get('special_chars')):
            characters.extend(list(special))
        for i in range(length):
            password += random.choice(characters)
        return render(request,'pwd_generator.html',{"password":password})
    # else:
    #     return render(request,'pwd_generator.html')