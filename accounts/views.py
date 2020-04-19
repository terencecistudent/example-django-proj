from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegisterForm, UpdateForm
from checkout.models import UserOrder


def index(request):
    """
    Returns to the homepage/index.html
    """
    return render(request, "index.html")


def register(request):
    """
    Renders the registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password1"])

            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request,
                    "Registration successful, you are now signed in!"
                )
                return redirect(reverse("index"))
            else:
                messages.error(
                    request,
                    "Account registration not availiable at this time."
                )
    else:
        register_form = RegisterForm()

    return render(request, "register.html", {
                    "register_form": register_form}
                  )


def login(request):
    """
    Log in page for users
    """
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password"])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are now signed in!")
                return redirect(reverse("index"))
            else:
                login_form.add_error(None, "Incorrect username or password")

    else:
        login_form = LoginForm()

    return render(request, "login.html", {"login_form": login_form})


@login_required
def logging_out(request):
    """
    Signs a user out when they are logged in
    """
    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect(reverse("index"))


def user_profile(request):
    """
    Profile page showing user's details
    and orders
    """
    user = User.objects.get(email=request.user.email,
                            username=request.user.username)
    return render(request, "user_profile.html", {"profile": user})


def update_user_info(request, id):
    user = get_object_or_404(User, pk=id)
    if user.id != request.user.id:
        return redirect("index")
    else:
        if request.method == "POST":
            form = UpdateForm(request.POST, request.FILES,
                              id, instance=user)

            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                messages.success(
                    request, "You have successfuly edited your information!")
                return redirect(user_profile, user.id)
        else:
            form = UpdateForm(instance=user)
    return render(request, 'user_profile.html', {'form': form}, {'user': user},)
