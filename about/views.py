from django.shortcuts import render


def about(request):
    """
    Renders the about.html page
    """
    return render(request, "about.html")
