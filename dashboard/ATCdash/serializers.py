from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

    def create(self, validated_data):
        # Ensure username and email are unique
        username = validated_data.get('username')
        email = validated_data.get('email')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'This username already exists'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email address is already in use'})

        # Hash the password before saving
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password if it exists
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)
