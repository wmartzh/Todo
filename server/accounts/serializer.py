from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    

    def create(self, validate_data):

        user = CustomUser(
            username=validate_data['username'],
            email = validate_data['email'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user
