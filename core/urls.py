from django.urls import path
from core import views
from rest_framework import routers
from core.rest_views import CompanyViewSet


app_name = "shared"

router = routers.SimpleRouter()
router.register(r"companies", CompanyViewSet)


urlpatterns = [
    path("hello/", views.hello, name="hello"),
]
