from django.urls import path
from . import views
from . import jobs

urlpatterns = [
    path(r'', views.index.as_view())
]
