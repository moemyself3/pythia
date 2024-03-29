from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import SignupUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, ("Login Successful. Welcome!"))
            return redirect("dashboard:index")
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, ("There was an error logging in. Try Again."))
            return redirect("users:login")
    else:
        return render(request, 'users/authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out. Clear Skies!"))
    return redirect("dashboard:index")


def signup(request):
    if request.method == "POST":
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Sign up successful!"))
            return redirect("dashboard:index")

    else:
        form = SignupUserForm(label_suffix="")

    return render(request, 'users/authenticate/signup.html', {'form': form,}) 
