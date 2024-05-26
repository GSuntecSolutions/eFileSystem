# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from .forms import EditForm
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                user_name = request.session.get('username', None)
                usernames = User.objects.values_list('username', flat=True)
                request.session['usernames'] = list(usernames)
                usernames = request.session.get('usernames', [])
                # Print all usernames
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def logout_view(request):

    return render(request, "accounts/login.html")

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url="/login/")
def get_users(request):

            # username = form.cleaned_data['username']
            # password = form.cleaned_data["password1"]
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # return redirect('user_list')
    userlist = list(User.objects.values())
    # for user in list(userlist):
    for user in userlist:
        del user["password"]
    # print(userlist)
    form = RegisterForm()
    # if request.errors:
    # print(request)
    context = {"users": userlist, "form": form, "message": ""}
    
    return render(request, "accounts/adduser.html", context)


@login_required(login_url="/login/")
def create_user(request):
    # print('crete')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # print('Form data:', form.data, form.is_valid())
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data["password1"]
            # user = authenticate(username=username, password=password)
            # login(request, user)
            message = "User Created Successfully"
            # print(message)
            # request.method="GET"
            form = RegisterForm()
            result = "success"
        else:

            message = form.errors
            result = "error"
            # print(message)
        return JsonResponse({"status": "success",  "message": message, "result": result })
@login_required(login_url="/login/")
def edit_user(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        # print('Form data:', form.data, form.is_valid())
        if form.is_valid():
            # user_id = form.data.get(user_id)
            user_id = form.cleaned_data.get('user_id')
            # print('user', user)
            try:
                user = User.objects.get(id=user_id)
                # print('user', user)
                form = EditForm(request.POST, instance=user)
                form.save()
                response_data = {'result': 'success'}
            except User.DoesNotExist:
                response_data = {'result': 'error', 'message': 'User not found'}
            # form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data["password1"]
            # user = authenticate(username=username, password=password)
            # login(request, user)
            message = "User Created Successfully"
            # print(message)
            # request.method="GET"
            form = EditForm()
            result = "success"
        else:

            message = form.errors
            result = "error"
            # print(message)
        return JsonResponse({"status": "success",  "message": message, "result": result })
    

@login_required(login_url="/login/")
def delete_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        
        try:
            user = User.objects.get(id=user_id)
            userId = int(user_id)
            # print('userId', userId)
            user.delete()
            # users_to_update = User.objects.filter(int(id) > userId)
            # print('users_to_update', users_to_update)
            # for user in users_to_update:
            #     user.id -= 1
            #     user.save()
            return JsonResponse({'message': 'User deleted successfully'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

from .forms import UserForm


@csrf_exempt
@require_POST
def update_user(request):
    if request.method == 'POST':
        # print('request')
        data = json.loads(request.body)
        user_id = data.get('user_id')
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        is_superuser = data.get('is_superuser')
        is_staff = data.get('is_staff')
        # print('is---->', is_staff, is_superuser)
        try:
            user = User.objects.get(id=user_id)
            user.username = username
            user.first_name=first_name
            user.last_name=last_name
            user.email = email
            user.is_superuser = is_superuser
            user.is_staff = is_staff
            user.save()
            # user.delete()
            return JsonResponse({'message': 'User Edit successfully'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
