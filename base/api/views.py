from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from  rest_framework import generics

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    

# class BlogPeirView(generics.ListAPIView):
#     serializer_class = 






@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        '/api/token',
        '/api/token/refersh'
    ]
    
    return Response(routes)