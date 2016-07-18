from .forms import UserCreateForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
            
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'register.html', context)
    
    
def login_user(request):
    form = AuthenticationForm(data=request.POST or None)    # must use "data=" with AuthenticationForm or won't work.
    if request.method == 'POST':        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)        
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home_page')
    context = {'form': form}
    return render(request, 'login_user.html', context)
    
    
@login_required           
def logout_user(request):
    logout(request)
    return redirect('home_page')
    
    
    
# user login with no form.
# def login_user(request):
    # if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)
        # if user is not None:
            # if user.is_active:
                # login(request, user)
                # return redirect('list')
            # else:
                # message.warning(request, 'Your Account Is Disabled')
        # else:
            # message.warning(request, 'Please Provide A Valid Username Or Password')