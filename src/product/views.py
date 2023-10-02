from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import getAllProductSerializer, ProductSerializer
from datetime import datetime
# Create your views here.

class getAllProducts(APIView):
    serializer_class = ProductSerializer
    def get(self,request):
        list_products = Product.objects.all()
        mydata = getAllProductSerializer(list_products, many=True)
        return Response(data = mydata.data, status=status.HTTP_200_OK)
   

    def post(self, request, format=None):
        # Sử dụng serializer để kiểm tra và lưu sản phẩm từ dữ liệu POST
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Ban vui long nhap lai", status=status.HTTP_400_BAD_REQUEST)
    

    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            return None    

    # method path   
    def patch(self, request, pk):
        product = self.get_product(pk)
        if product == None:
            return Response({"status": "404", "message": f"Product with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"product": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        product = self.get_product(pk)
        if product == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)