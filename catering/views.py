from django.shortcuts import render
from django.http import HttpResponse
from .models import package,Contact
from django.contrib import messages

# Create your views here.

def index(request):
     return render(request,'index.html')
def events(request):
    return render(request,'events.html')
def packages(request):
   packs=package.objects.all()
   return render(request,'packages.html',{'packs':packs})    
def supplies(request):
    return render(request,'supplies.html')
def menu(request):
    return render(request,'menu.html') 
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    if request.method == 'POST':
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact(name=name, email=email, phone=phone, desc=desc).save()
        messages.success(request, "Thank you for your response. We will be in touch with you as soon as possible.")
    return render(request, 'contactus.html')# def cart(request):
#     return render(request,'cart.html')              
                   
                  
   

