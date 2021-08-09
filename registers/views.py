from django.shortcuts import redirect, render
from .forms import UserRegisterView, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
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
    context ={'form': form}
    return render(request, 'registration/login.html', context)
