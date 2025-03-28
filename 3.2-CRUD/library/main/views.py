from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request): # Получение списка книг
    """получите список книг из БД, отсериализуйте и верните ответ."""
    books = Book.objects.all()  # Получаем все книги из БД
    serializer = BookSerializer(books, many=True)  # Сериализуем список книг
    return Response(serializer.data)  # Возвращаем сериализованные данные

class CreateBookView(APIView): # Создание книги
    def post(self, request):
        serializer = BookSerializer(data=request.data)  # Передаем данные из запроса в сериализатор
        if serializer.is_valid(raise_exception=True): # Если данные валидны
            serializer.save()  # Сохраняем книгу
            return Response({'message': 'Книга успешно создана', 'book': serializer.data}, status=status.HTTP_201_CREATED)  # Возвращаем ответ об этом

class BookDetailsView(RetrieveAPIView):  # Получение деталей книги
    queryset = Book.objects.all()  # Определяем queryset
    serializer_class = BookSerializer  # Указываем сериализатор

class BookUpdateView(UpdateAPIView):  #О бновление книги
    queryset = Book.objects.all()  # Определяем queryset
    serializer_class = BookSerializer  # Указываем сериализатор

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Позволяем частичное обновление
        instance = self.get_object()  # Получаем объект
        serializer = self.get_serializer(instance, data=request.data, partial=partial)  # Сериализуем данные
        serializer.is_valid(raise_exception=True)  # Проверяем валидность
        self.perform_update(serializer)  # Сохраняем изменения
        return Response(serializer.data)  # Возвращаем сериализованные данные

class BookDeleteView(DestroyAPIView):  # Удаление книги
    queryset = Book.objects.all()  # Определяем queryset
    serializer_class = BookSerializer   # Указываем сериализатор

class OrderViewSet(viewsets.ModelViewSet):  # создадим `OrderViewSet`
    queryset = Order.objects.all()  # Определяем queryset
    serializer_class = OrderSerializer  # Указываем сериализатор
