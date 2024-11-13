from rest_framework.decorators import api_view
from rest_framework.response import responses
from rest_framework import status
from.models import user
from .serializer import userserializer


@api_view('GET')
def get_user(request):
      return responses(userserializer({'name':"dipak", "age":23}).data)
@api_view('POST')
def create_user(request):
     serializer = userserializer(data=request.data)
     if serializer.is_valid():
           serializer.save()
           return responses(serializer.data, status=status.HTTP_201_CREATED)
     return responses(serializer.errors, status=status.HTTP_400_BAD_REQUEST)