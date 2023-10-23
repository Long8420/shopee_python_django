from rest_framework import serializers
from .models import Category, Product

class getAllProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class getAllCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# C1 ke thua tu modelSerializer 
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'  # Để bao gồm tất cả các trường của Product
    
# c2 custom fields ke thua tu Serializer  cac truong can them 
class ProductSerializer(serializers.Serializer):
    # Định nghĩa các trường tùy chỉnh ở đây
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.IntegerField()
    product_img = serializers.CharField(max_length=255)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Sử dụng PrimaryKeyRelatedField để đối ứng với khoá ngoại
    # Định nghĩa phương thức create() để lưu sản phẩm
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

        
    def update(self, instance, validated_data):
        # Cập nhật các trường của instance dựa trên validated_data
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.product_img = validated_data.get('product_img', instance.product_img)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class CategoriSerializer(serializers.Serializer):
   title = serializers.CharField(max_length=255)
   slug = serializers.CharField(max_length=255)
   description = serializers.CharField()

   def create(self, validated_data):
        return Category.objects.create(**validated_data)

   def update(self, instance, validated_data):
    # Cập nhật các trường của instance dựa trên validated_data
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance