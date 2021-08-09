from django.shortcuts import redirect, render
from .forms import UserRegisterView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def CreateUser(request):
    form = UserRegisterView()
    if request.method == "POST":
        form = UserRegisterView(request.POST)
        if form.is_valid:
            form.save()
        

    context = {"form": form}
    return render(request, 'registration/register.html', context)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaneed_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('index.html')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    context ={'form': form}
    return render(request, 'registration/login.html', context)
