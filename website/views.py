from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.contrib.messages.api import error
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, TemplateView
from .models import Record
from .forms import AddRecordForm


# Create your views here.

def home(request):
    records = Record.objects.all()
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Well Done CNZ Team!")
            return redirect('user:home')
        else:
            messages.success(request,"There was an Error Logging In, Please Try again !")
            return redirect('user:home')
    else:
        return render(request,'home.html',{'records':records})


def logout_request(request):
    logout(request)
    messages.success(request,"See you next time... Team")
    return redirect('user:home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"You have Successfully!")
            return redirect('user:home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})

    return render(request, 'register.html', {'form': form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You Must be Logged In !")
        return redirect('user:home')



def delete_record(request,pk):
   if request.user.is_authenticated:
      delete_it = Record.objects.get(id=pk)
      delete_it.delete()
      messages.success(request, "Record deleted Successfully...")
      return redirect('user:home')
   else:
      messages.success(request, "You Must be Logged In To Do That..")
      return redirect('user:home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record Added...")
                return redirect('user:home')
        return  render(request,'add_record.html',{'form':form})
    else:
        messages.success(request, "You Must Be logged In...")
        return redirect('user:home')


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated! ")
            return redirect('user:home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request, "You Must Be logged In...")
        return redirect('user:home')