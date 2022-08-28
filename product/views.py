from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from product.serializer import ProductSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'brand', 'category']
    ordering_fields = ['price', 'discountPercentage', 'rating', 'stock']
    
class ProductCreate(APIView):
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProductDetail(APIView):

    def get(self, request, pk):
        try:
            serializer = ProductSerializer(Product.objects.get(pk=pk))
            return Response(serializer.data)
        except:
            return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, pk):
        try:
            Product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(Product, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            Product = Product.objects.get(pk=pk)
            Product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)