from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import UserProfile
from recipes.models import UserRecipe
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name          = request.POST['first_name']
        last_name           = request.POST['last_name']
        username            = request.POST['username']
        email               = request.POST['email']
        password            = request.POST['password']
        confirm_password    = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('register')
        
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('register')
        
        else:
            if password==confirm_password:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                return redirect('login')
            else:
                messages.info(request,'password does not match')
                return redirect('register')
            
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    context ={
        'userprofile': userprofile,
    }
    return render(request, 'accounts/profile.html', context)

def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    userrecipes = get_object_or_404(UserRecipe,  user=request.user)
    context ={
        'userprofile': userprofile,
        'userrecipes': userrecipes,
    }
    if request.method == 'POST':
        first_name      = request.POST['first_name']
        last_name       = request.POST['last_name']
        username        = request.POST['username']
        email           = request.POST['email']
        mobile          = request.POST['mobile']
        address_line_1  = request.POST['address_line_1']
        address_line_2  = request.POST['address_line_2']
        city            = request.POST['city']
        state           = request.POST['state']
        country         = request.POST['country']

        user = User.objects.get(id=userprofile.user_id)

        user.first_name = first_name
        user.last_name  = last_name
        user.username   = username
        user.email      = email

        userprofile.mobile          = mobile
        userprofile.address_line_1  = address_line_1
        userprofile.address_line_2  = address_line_2
        userprofile.city            = city
        userprofile.state           = state
        userprofile.country         = country
        
        user.save()
        userprofile.save()


        return redirect('profile')
    else:
        return render(request, 'accounts/edit_profile.html', context)
    

