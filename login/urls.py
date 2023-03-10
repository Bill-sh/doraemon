from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'', views.AuthViewSet, basename='auth')

urlpatterns = router.urls
