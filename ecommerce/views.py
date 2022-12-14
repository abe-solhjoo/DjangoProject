from django.contrib.auth import authenticate, login
from .forms import ContactForm, LoginForm
from django.shortcuts import render, redirect


def home_page(request):
    context = {
        'title': 'صفحه اصلی',
        'content': 'به سایت ما خوش آمدید'
    }
    return render(request, "home_page.html", context)


def about_us(request):
    context = {
        'title': 'درباره ما',
        'content': 'ما در حال توسعه هستیم'
    }
    return render(request, "about_us.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'contact us',
        'content': 'Contact us',
        'form': contact_form
    }
    if contact_form.is_valid():
        result = contact_form.cleaned_data
        print(result)
        for v in result.values():
            print(v)
    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('message'))
    return render(request, 'contact/view.html', context)


def login_form(request):
    print(f"The user authentication is: {request.user.is_authenticated}")
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            context["form"] = LoginForm()
            return redirect('/')
        else:
            print("Error")

    return render(request, "auth/login.html", context)


def register_form(request):
    return render(request, "auth/register.html", {})
