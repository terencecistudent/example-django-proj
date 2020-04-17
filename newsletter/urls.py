from django.conf.urls import url
from .views import newsletter


urlpatterns = [
    url(r'^subscribe/', newsletter, name="newsletter"),
]
