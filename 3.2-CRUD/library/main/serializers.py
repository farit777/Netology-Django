from rest_framework import serializers
from main.models import Book, Order

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'year']  # Указываем поля, которые должны быть сериализованы

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_name', 'days_count', 'date', 'books']  # Указываем поля, которые должны быть сериализованы
