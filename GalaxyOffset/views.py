from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.forms.models import model_to_dict
from .forms import CreateUserForm, EditUserProfile
from .models import *
import json


def index(request):
    return render(request, 'GalaxyOffset/index.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username or Password is incorrect')
                return redirect('login')

        context = {}
        return render(request, 'GalaxyOffset/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'GalaxyOffset/register.html', context)


def editUser(request):
    if request.user.is_authenticated:
        form = EditUserProfile(request.POST, request.FILES, instance=request.user)
        if request.method == 'POST':
            form = EditUserProfile(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('view-profile')

        context = {'form': form}
        return render(request, 'GalaxyOffset/edit_profile.html', context)

    else:
        return redirect('login')


def aboutUs(request):
    return render(request, "GalaxyOffset/about.html")


def packages(request):
    return render(request, "GalaxyOffset/packages.html")


def feedback(request):
    if request.user.is_authenticated:
        return redirect('feedback')
    else:
        return redirect('login')


def order(request):
    return render(request, "GalaxyOffset/order.html")


def product(request, id):
    products = Product.objects.get(prod_ID=id)
    print(products)
    sizesmap = SizeProductMapping.objects.filter(prod_id=id)

    # print(sizesmap)
    # for data in sizesmap:
    #     sizes = data.size_id
    #     print(sizes.prod_size)

    # for data in sizesmap:
    #     dict_obj = model_to_dict(data)
    #     serialized = json.dumps(dict_obj)
    #     print(serialized)
    #     sizes=data.size_id
    #     print(sizes.prod_size)
    # return HttpResponse(sizesmap)
    return render(request, "GalaxyOffset/product.html", {'products': products})


def view_profile(request):
    return render(request, "GalaxyOffset/profile.html")


def edit_profile(request):
    return render(request, "GalaxyOffset/edit_profile.html")


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                return redirect('view-profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'GalaxyOffset/change_password.html', {
            'form': form
        })
    else:
        return redirect('login')
