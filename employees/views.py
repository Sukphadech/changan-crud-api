from rest_framework import viewsets
from .models import Employee, Department, Position, Status
from .serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    PositionSerializer,
    StatusSerializer,
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()
    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "department",
        "position",
        "status",
    ]

    search_fields = [
        "name",
        "address",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]
    permission_classes = [IsAuthenticated]
    
    