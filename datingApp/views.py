# datingApp/views.py
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, RegisterSerializer

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
#from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id = request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer