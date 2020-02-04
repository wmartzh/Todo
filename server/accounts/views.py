from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .responses import ResponseHelper

from .models import CustomUser
from .serializer import UserSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if username is None:
        return ResponseHelper.emptyField('username')
    elif email is None:
        return ResponseHelper.emptyField('email')
    elif password is None:
        return ResponseHelper.emptyField('password')
    
    queryset = CustomUser.objects.create_user(
       username=username, email=email,password=password)
    
    serializer = UserSerializer(queryset)

    return Response(serializer.data,status=200)
   

