from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets, permissions
from rest_framework.generics import ListAPIView
from .serializers import EmployeeSerializer

from .models import ForTest


class EmployeeView(ListAPIView):
    queryset = ForTest.objects.all()
    serializer_class = EmployeeSerializer

class SearchView(generics.ListAPIView):
    queryset = ForTest.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'surname']

class FilterView(generics.ListAPIView):
    queryset = ForTest.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'surname', 'patronymic', 'position', 'date_of_receipt', 'salary']

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ForTest.objects.all()