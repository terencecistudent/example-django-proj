from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import register, index, login, logging_out, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'register/', register, name="register"),
    url(r'logout/', logging_out, name="logging_out"),
    url(r'login/', login, name="login"),
    url(r'profile/', user_profile, name="user_profile"),
    url(r'password-reset/', include(url_reset)),
]
