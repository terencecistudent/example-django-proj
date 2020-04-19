from django.conf.urls import url, include
from accounts.views import register, login, logging_out, user_profile, update_user_info
from accounts import url_reset

urlpatterns = [
    url(r'register/', register, name="register"),
    url(r'logout/', logging_out, name="logging_out"),
    url(r'login/', login, name="login"),
    url(r'profile/', user_profile, name="user_profile"),
    url(r'^profile/(?P<id>\d+)/edit/$', update_user_info, name="update_user_info"),
    url(r'password-reset/', include(url_reset)),
]
