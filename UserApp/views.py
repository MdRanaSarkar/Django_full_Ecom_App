from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from Product.models import Category, Product, Images
from django.contrib import messages
from EcomApp.models import Setting
from UserApp.forms import SignUpForm
from UserApp.models import UserProfile
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)

    context = {'category': category,
               'setting': setting}
    return render(request, 'user_login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')



def user_register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password_raw=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password_raw)
            login(request,user)
            current_user=request.user
            data =UserProfile()
            data.user_id=current_user.id
            data.image="user_img/avatar.jpg"
            data.save()



            return redirect('home')
        else:
            messages.warning(request,"Your new and reset password is not matching")
    else:
        form=SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={'category': category,
               'setting': setting,
               'form':form}
    return render(request,'user_register.html',context)


def userprofile(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)

    context={'category': category,
               'setting': setting,
               'profile':profile}
    return render(request,'user_profile.html',context)

