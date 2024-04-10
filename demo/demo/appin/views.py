from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Datas

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def home(request):  # 127.0.0.1:8000/
    mydata=Datas.objects.all()
    if(mydata!=""):
        return render(request,"home.html",{"datas":mydata})
    else:
        return render(request,"home.html")    

def register(request):
    if request.method=="POST":
        firstname=request.POST["name"]
        age=request.POST["age"]
       
        address=request.POST["address"]
        mail=request.POST["mail"]
        
        obj=Datas()
        obj.Name=firstname
        obj.Age=age
 
        obj.Address=address
        obj.Mail=mail
        obj.save()
        mydata=Datas.objects.all()
        return redirect("home")
    return render(request,"home.html")

