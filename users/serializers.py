from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    ROLE_CHOICES = ('staff', 'admin')

    role = serializers.ChoiceField(choices=ROLE_CHOICES, write_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'role']

    def validate_email(self, value):
          if User.objects.filter(email=value).exists():
               raise serializers.ValidationError('Email already exists')
          return value


    def create(self, validated_data):
        role = validated_data.pop('role')

        if role == 'admin':
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_staff(**validated_data)
