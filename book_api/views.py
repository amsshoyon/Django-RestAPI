from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.filters import SearchFilter
from rest_framework import generics


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    
class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookDetail(APIView):

    def get(self, request, pk):
        try:
            serializer = BookSerializer(Book.objects.get(pk=pk))
            return Response(serializer.data)
        except:
            return Response({'error': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)