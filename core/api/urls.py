from rest_framework import routers

from core.api.views import CompanyViewSet


router = routers.SimpleRouter()
router.register(r"companies", CompanyViewSet)

urlpatterns = router.urls
