from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'student', views.StudentsViewSet, basename='student')
router.register(r'class', views.ClassNameViewSet, basename='class')

urlpatterns = [
    path('', include(router.urls)),
]
