from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages
# Create your views here.

def chpass(request):
    if request.method == "POST":
        cp = request.POST.get("cpass")
        if check_password(cp, request.user.password):
            np = request.POST.get("npass")
            request.user.set_password(np)
            request.user.save()
            return redirect("acc:login")
        else:
            pass # 마지막날
    return render(request, "acc/chpass.html")

def update(request):
    if request.method == "POST":
        u = request.user
        ue = request.POST.get("umail")
        up = request.FILES.get("upic")
        uc = request.POST.get("ucom")
        u.email, u.comment = ue, uc
        if up:
            u.pic.delete()
            u.pic = up
        u.save()
        return redirect("acc:profile")

    return render(request, "acc/update.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        ue = request.POST.get("umail")
        uc = request.POST.get("ucom")
        upic = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, email=ue, comment=uc, pic=upic)
            return redirect("acc:login")
        except:
            messages.info(request, "username 이 중복되어 계정을 생성할 수 없습니다")
    return render(request, "acc/signup.html")

def delete(request):
    if request.method == "POST":
        cp = request.POST.get("cpass")
        if check_password(cp, request.user.password):
            request.user.pic.delete()
            request.user.delete()
            return redirect("acc:index")
    return render(request, "acc/delete.html")


def profile(request):
    return render(request, "acc/profile.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def index(request):
    return render(request, "acc/index.html")
def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u :
            login(request, u)
            messages.success(request, f"{un} 님 환영합니다!!")
            return redirect("acc:index")
        else:
            messages.info(request, "회원정보가 일치하지 않습니다")
    return render(request, "acc/login.html")