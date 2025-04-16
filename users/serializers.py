from rest_framework import serializers
from .models import User, Profile, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'friends']
        extra_kwargs = {
            'friends': {'required': False}  # Теперь поле необязательное
        }



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'