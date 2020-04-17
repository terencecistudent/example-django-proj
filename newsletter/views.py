from django.shortcuts import render, redirect
from .models import Newsletter
from .forms import NewsletterForm
from django.contrib import messages


def newsletter(request):
    subscribe = NewsletterForm(request.POST)
    if subscribe.is_valid():
        instance = subscribe.save(commit=False)
        if Newsletter.objects.filter(email=instance.email).exists():
            messages.warning(request, "You have already subscribed!")
        else:
            instance.save()
            messages.success(request, "You have subscribed!")
    return render(request, "login.html", {"subscribe": subscribe})
