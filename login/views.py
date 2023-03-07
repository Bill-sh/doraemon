# Create your views here.
import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny

from login.serializers import AuthSerializer


class AuthViewSet(ViewSet):
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny]

    def list(self, request):
        username, password = request.query_params.get('username'), request.query_params.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                'id': user.id,
                'name': user.get_full_name().replace(' ', ''),
            })
        else:
            return Response({
                'detail': '用户名或密码错误'
            }, status=403)
