from rest_framework import viewsets
from core.models import Company
from core.api.serializers import CompanySerializer
from core.api.permissions import HasStaffPermission


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [HasStaffPermission]
