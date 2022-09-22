from rest_framework import generics, permissions, viewsets
from apps.catalog.models import Product, Category, Image
from apps.api.catalog.serializers import ProductReadSerializer, ProductWriteSerializer, ImageSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()


class ProductUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()


class ProductDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
