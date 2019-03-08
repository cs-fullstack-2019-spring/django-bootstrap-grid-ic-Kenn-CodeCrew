from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "BootGridApp/signIn.html")


def signIn(request):
    return render(request, "BootGridApp/signIn.html")


def signUp(request):
    return render(request, "BootGridApp/signUp.html")
