from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from django.http import Http404

class booksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serial=BookSerializer(books, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=BookSerializer(data=request.data)
        print(request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class booksPUT(APIView):   

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404


    def put(self, request, pk):
        # print(pk)
        book = self.get_object(pk)
        serial = BookSerializer(book, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
