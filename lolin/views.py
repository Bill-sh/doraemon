from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from lolin.filters import StudentsFilter
from lolin.models import Students, ClassName
from lolin.serializers import StudentsSerializer, ClassNameSerializer


class ClassNameViewSet(ModelViewSet):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class StudentsViewSet(ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = StudentsFilter
    ordering_fields = ['name', 'className']
    ordering = ['className', 'name']
