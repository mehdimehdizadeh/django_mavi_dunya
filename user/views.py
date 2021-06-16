from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from article.models import Category

# Create your views here.
def register(request):
    category = Category.objects.all()
    form = RegisterForm(request.POST or None)
    context = {
        "form":form,
        "categories":category,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        mail = form.cleaned_data.get("mail")
        if User.objects.filter(username = username).first():
            messages.info(request,"Bu istifadəçi adı artıq mövcuddur!")
            return render(request,"register.html",context)
        newUser = User(username = username,email = mail)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect("index")
    return render(request,"register.html",context)
def loginUser(request):
    category = Category.objects.all()
    form = LoginForm(request.POST or None)
    context = {
        "form":form,
        "categories":category,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request,"Istifadəçi adı və ya şifrə yalnışdır!")
            return render(request,"login.html",context)
        messages.success(request,"Giriş doğrulandı!")
        login(request,user)
        return redirect("index")
    

    return render(request,"login.html",context)
@login_required(login_url="user:login")
def logoutUser(request):
    logout(request)
    messages.success(request,"Çıxış edildi!")
    return redirect("index")

