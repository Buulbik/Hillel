from rest_framework import serializers
from apps.catalog.models import Category, Product, Image


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'image',
            'meta_title',
            'meta_description',
            'meta_keywords',
        )


class ProductWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
        )


class ProductReadSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    main_image = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    def get_main_image(self, obj):
        serializer = ImageSerializer(obj.main_image(), context=self.context)
        return serializer.data

    def get_images(self, obj):
        try:
            images = obj.images().exclude(id=obj.main_image().id)
            serializer = ImageSerializer(images, context=self.context, many=True)
            return serializer.data
        except AttributeError:
            return None

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'categories',
            'main_image',
            'images'
        )


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'image',
            'product',
            'is_main',
        )
