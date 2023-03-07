from django_filters.rest_framework import FilterSet

from lolin.models import Students


class StudentsFilter(FilterSet):
    class Meta:
        model = Students
        fields = []