from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import UserModel
from .serializers import RegisterUserSerializer, UserSerializer
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response



class UserView(APIView):    
    def get(self, request, id=None):
        if id:
            user = get_object_or_404(UserModel, user_id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def put(self, request, id):
        user = get_object_or_404(UserModel, user_id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    def patch(self, request, id):
        user = get_object_or_404(UserModel, user_id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User partially updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        user = get_object_or_404(UserModel, user_id=id)
        user.delete()
        return Response({'message': 'User permanently deleted'})



@api_view(["POST",])
@permission_classes([AllowAny]) 
def register_view(request):
    
    if request.method == "POST":
        serializer = RegisterUserSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration successful!"
            data['username'] = account.username
            data['email'] = account.email
        
        else:
            data = serializer.errors
            
        return Response(data)
    
@api_view(["POST",])
@permission_classes([IsAuthenticated])
def logout_view(request):
    
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
