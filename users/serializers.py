from rest_framework import serializers
from django.contrib.auth.hashers import make_password  # To hash the password
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'  # You can adjust this as per your fields
    
    def create(self, validated_data):
        # Hash the password before saving
        password = validated_data.pop('password')
        user = UserModel.objects.create(
            **validated_data,
            password_hash=make_password(password)  # Hash the password manually
        )
        return user





class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # Exclude user_id as it's auto-generated, and password_hash to hash it properly
        fields = ['username', 'email', 'password', 'role', 'profile_image_url', 'phone_number', 'address', 'ai_order_preferences']

    def save(self, **kwargs):
        
        password = self.validated_data['password']
        
        if UserModel.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email already exists!"})
        
        account = UserModel(email=self.validated_data["email"], 
                       username=self.validated_data['username'],)
        account.set_password(password)
        
        account.save()
        
        return account