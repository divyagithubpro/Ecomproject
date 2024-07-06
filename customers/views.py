from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
from . models import Customer
# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')


def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
                
                #create user account 
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
                )
                
                
                # create cust account
            customer=Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
                )
            success_message="user registered successfully"
            messages.error(request,success_message)
        except Exception as e:
            error_message="Duplicate username or invalid credentials"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register']=False

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message="invalid user"
            messages.error(request,error_message)

    return render(request, 'account.html',context)