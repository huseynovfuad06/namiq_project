from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import get_user_model, login, authenticate


User = get_user_model()

# Create your views here.


def login_view(request):
    context = {}
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)

            login(request, user)
            
            return redirect('/')
    
    context["form"] = form
    return render(request, "accounts/login.html", context)