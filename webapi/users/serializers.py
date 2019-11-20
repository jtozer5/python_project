from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'description', 'img_profile')
        write_only_fields = ('password',)