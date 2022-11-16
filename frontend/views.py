from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/signin')
    return render(request,'register.html', {'form':form})

@login_required(login_url='/signin')
def tasks(request):
    user= request.user
    context = {'user':user}
    return render(request, 'tasks.html',context)


def signin(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form= AuthenticationForm(request)
    return render(request,'login.html',{'form':form})

@login_required(login_url='/signin')
def signout(request):
    if request.method=='POST':
        logout(request)
    return redirect ('/signin')