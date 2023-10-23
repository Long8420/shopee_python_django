from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import getAllProductSerializer, ProductSerializer, getAllCategorySerializer, CategoriSerializer
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# API Category

class apiCategory(APIView):
    def get_queryset(self):
            category = Category.objects.all()
            return category

    def get_object(self, id):
        return get_object_or_404(self.get_queryset(), id=id)

    def get(self, request, pk=None, *args, **kwargs):
        id = pk or request.query_params.get('id') 
        #c1  
        # try:
        #      # id = request.query_params["id"]
        #     id = self.kwargs["pk"]
        #     if id != None:
        #         category_obj = Category.objects.get(id=id)
        #         serializer = getAllCategorySerializer(category_obj)
        # except:
        #     # list_category = Category.objects.all()
        #     list_category = self.get_queryset()
        #     serializer = getAllCategorySerializer(list_category, many=True)
        if id:
            serializer = getAllCategorySerializer(self.get_object(id))
        else:
            serializer = getAllCategorySerializer(self.get_queryset(), many=True)
        return Response(data = serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        chech_request = CategoriSerializer(data=request.data)
        if chech_request.is_valid():
            chech_request.save()
            return Response(chech_request.data, status=status.HTTP_201_CREATED)
        return Response("Ban vui long nhap lai", status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk=None, *args, **kwargs):
        category_object = self.get_object(pk or request.query_params.get('id'))
        serializer =CategoriSerializer (
            category_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":status.HTTP_200_OK, "data": {"category": serializer.data}})
        return Response("Ban vui long nhap lai", status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response({"success":"xoa thanh cong", "status":status.HTTP_204_NO_CONTENT})
# API  product
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
