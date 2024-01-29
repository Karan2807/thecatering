from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def signup(request):

    if request.method =='POST':
        name= request.POST['name']
        email= request.POST['email']
        username= request.POST['username']
        pass1= request.POST['pass1']
        pass2 = request.POST['pass2']
        add=request.POST['add'] 

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('signup')
            else:    
                 user=User.objects.create_user(first_name=name,email=email,username=username,password=pass1)
                 user.save();
                 messages.info(request,'User Created')
                 return redirect('login')
                 
        else:
             messages.info(request,'Password Not Matching')
        return redirect('/')   
    else:    
        return render(request,'signup.html')  

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username,password=password)
         
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid  Credentials')    
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')        