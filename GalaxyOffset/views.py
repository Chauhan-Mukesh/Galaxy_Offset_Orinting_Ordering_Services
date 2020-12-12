from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import CreateUserForm, EditUserProfile
from .models import *


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
    sizeslist = []
    AqutousCoatingProductlist = []
    Colorslist = []
    PaperChoiceProductslist = []
    ShrinkWrappingProductslist = []
    FoldingOptionsProductslist = []
    NoOfMonthsProductslist = []
    HoleDrillingProductslist = []
    BindingMethodProductslist=[]

    try:
        sizesmap = SizeProductMapping.objects.filter(prod_id=id)
        sizeslist = [data.size_id.prod_size for data in sizesmap]
    except AttributeError:
        pass

    try:
        colormap = ColorProductMapping.objects.filter(prod_id=id)
        Colorslist = [data.color_id.prod_color for data in colormap]
    except AttributeError:
        pass

    try:
        PaperChoiceProductmap = PaperChoiceProductMapping.objects.filter(prod_id=id)
        PaperChoiceProductslist = [data.paper_id.paper_choices_name for data in PaperChoiceProductmap]
    except AttributeError:
        pass

    try:
        AqutousCoatingProductmap = AqutousCoatingProductMapping.objects.filter(prod_id=id)
        AqutousCoatingProductlist = [data.aqutous_coating_id.aqutous_coating_type for data in AqutousCoatingProductmap]
    except AttributeError:
        pass

    try:
        ShrinkWrappingProductsmap = SizeProductMapping.objects.filter(prod_id=id)
        ShrinkWrappingProductslist = [data.shrink_wrapping_id.shrink_options for data in ShrinkWrappingProductsmap]
    except AttributeError:
        pass

    try:
        FoldingOptionsProductsmap = FoldingOptionsProductMapping.objects.filter(prod_id=id)
        FoldingOptionsProductslist = [data.folding_options_id.folding_options_type for data in
                                      FoldingOptionsProductsmap]
    except AttributeError:
        pass

    try:
        NoOfMonthsProductsmap = NoOfMonthsProductMapping.objects.filter(prod_id=id)
        NoOfMonthsProductslist = [data.no_of_months_id.months for data in
                                  NoOfMonthsProductsmap]
    except AttributeError:
        pass

    try:
        HoleDrillingProductsmap = HoleDrillingProductMapping.objects.filter(prod_id=id)
        HoleDrillingProductslist = [data.hole_drilling_id.hole for data in
                                    HoleDrillingProductsmap]
    except AttributeError:
        pass

    try:
        BindingMethodProductsmap = BindingMethodProductMapping.objects.filter(prod_id=id)
        BindingMethodProductslist = [data.binding_method_id.binding_methods for data in
                                    BindingMethodProductsmap]
    except AttributeError:
        pass

    context = {'products': products,
               'sizeslist': sizeslist,
               "AqutousCoatingProductlist": AqutousCoatingProductlist,
               "Colorslist": Colorslist,
               "PaperChoiceProductslist": PaperChoiceProductslist,
               "ShrinkWrappingProductslist": ShrinkWrappingProductslist,
               "FoldingOptionsProductslist": FoldingOptionsProductslist,
               "NoOfMonthsProductslist": NoOfMonthsProductslist,
               "HoleDrillingProductslist": HoleDrillingProductslist,
               "BindingMethodProductslist":BindingMethodProductslist
               }
    return render(request, "GalaxyOffset/product.html", context)


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
