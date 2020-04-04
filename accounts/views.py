from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import LoginForm, RegisterForm


def index(request):
    """
    Returns to the homepage/index.html
    """
    return render(request, "index.html")


def register(request):
    """
    Renders the registration page
    """
    if request.user.is_authenticated():
        return redirect(reverse("index"))

    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password"])

            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request,
                    "Registration successfully, you are now signed in!"
                )
                return redirect(reverse("index"))
            else:
                messages.error(
                    request, "Account registration not availiable this time."
                )
        else:
            register_form = RegisterForm()

        return render(render, "registration.html", {
                      "register_form": register_form}
                      )
