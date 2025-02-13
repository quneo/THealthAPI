from rest_framework import serializers
from .models import User, FriendShip


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Хэшируем пароль
        user.save()
        return user


class FriendShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendShip
        fields = '__all__'
