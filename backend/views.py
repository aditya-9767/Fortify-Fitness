from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact


def index(request):
    return render(request, 'index.html')

def fitness(request):
    return render(request, 'fitness.html')

def blog(request):
    return render(request, 'blog.html')    

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')

def bmi(request):
    return render(request, 'bmi.html')

def whr(request):
    return render(request, 'whr.html')

def calories(request):
    return render(request, 'calories.html')

def heart(request):
    return render(request, 'heart.html')

def diabetes(request):
    return render(request, 'diabetes.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def blog4(request):
    return render(request, 'blog4.html')

def blog5(request):
    return render(request, 'blog5.html')

def blog6(request):
    return render(request, 'blog6.html')