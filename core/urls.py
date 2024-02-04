from django.urls import path, include

from core import views
from core.api.urls import urlpatterns as api_urlpatterns


app_name = "shared"


urlpatterns = [
    path("api/", include(api_urlpatterns), name="api"),
    path("hello/", views.hello, name="hello"),
]
