from rest_framework import serializers
from .models import CustomUser, Book, Author, Genre, Condition, BookRequest


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'


class BookRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRequest
        fields = '__all__'
