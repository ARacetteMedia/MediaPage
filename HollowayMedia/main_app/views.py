from django.shortcuts import render
from django.template import loader
from main_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def index(request):
    context_dict = {'text':'hiya','word':'womp, womp womp womp cats cats cars womp'}
    return render(request, 'main_app/index.html',context=context_dict)

def other(request):
    return render(request, 'main_app/other.html',context=None)

def registration(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'main_app/registration.html',
    {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('main_app:user_login'))

            else:
                return HttpResponse('Account is inactive')

        else:
            print('someone failed to login')
            print('Username : {} and password {}'.format(username,password))
            return HttpResponse('invalid login details')
    else:
        return render(request,'main_app/login.html',context={})

def special(request):
    return HttpResponse('youre logged in!')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_app:user_login'))
