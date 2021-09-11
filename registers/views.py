from django.shortcuts import redirect, render
from .forms import UserRegisterView, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.generic.edit import CreateView
# Create your views here.
class CreateUser(CreateView):
    form_class = UserRegisterView
    template_name = 'registration/register.html'

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

    # checking for user using ajax
class ValidateUsername(View):
    def get(self, request):
        username = request.GET.get('username', None)

        data = {
            'is_present': User.objects.filter(username_iexact=username).exists()
        }

        return JsonResponse(data)
