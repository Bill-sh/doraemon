# Create your views here.

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny

from login.serializers import AuthSerializer


class AuthViewSet(ViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]

    def list(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')

        user = authenticate(username=username, password=password)
        serializer = AuthSerializer(data=request.query_params, many=False)
        serializer.is_valid()
        if user is None:
            return Response({'error': 'Invalid credentials'})

        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'user':
                    {
                        'name': user.get_full_name().replace(' ', ''),
                        'groups': [i['name'] for i in list(user.groups.all().values('name'))]
                    }
            }
        )
