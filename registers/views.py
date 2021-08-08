from django.shortcuts import render
from .forms import UserRegisterView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def CreateUser(request):
    form = UserRegisterView()
    if request.method == "POST":
        form = UserRegisterView(request.POST)
        if form.is_valid:
            form.save()
        

    context = {"form": form}
    return render(request, 'registration/register.html', context)
