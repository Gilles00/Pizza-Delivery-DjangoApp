from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/fancy_login.html", {"message": None})
    context = {
        "user": request.user
    }
    if User.objects.get(username=request.user).is_staff:
        return render(request, "orders/admin.html", context) #TODO: route the user to the home pizza page if user or admin page if admin
    return render(request, "orders/user.html", context) #TODO: route the user to the home pizza page if user or admin page if admin


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/fancy_login.html", {"message": "Invalid credentials."})



def logout_view(request):
    logout(request)
    return render(request, "orders/fancy_login.html", {"message": "Logged out."})


def register_view(request):
    # if not request.user.is_authenticated:
        # return render(request, "orders/register.html", {"message": None})
    if request.method == 'POST':


        username=request.POST["username"]
        password=request.POST["password"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]

        # if any of the fields are blank - reregister
        for val in [username, password, first_name, last_name, email]:
            if val == '':
                return render(request, "orders/fancy_register.html", {"message": "fill in all fields"})

        user=User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        user.save()

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/fancy_register.html", {"message": "Invalid credentials."})

    return render(request, "orders/fancy_register.html", {"message": None})
