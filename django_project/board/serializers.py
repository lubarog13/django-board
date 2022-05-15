from rest_framework import serializers

from .models import Card, Board
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'username')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user