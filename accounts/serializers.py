from rest_framework import serializers
from .models import Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'email']


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Student.EMAIL_FIELD