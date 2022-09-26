from rest_framework import generics, permissions, viewsets
from apps.catalog.models import Product, Category, Image
from apps.api.catalog.serializers import ProductReadSerializer, ProductWriteSerializer,\
    ImageSerializer, CategorySerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductReadSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(is_checked=True)

        if self.request.query_params.get('category'):
            queryset = queryset.filter(categories=self.request.query_params['category'])

        if self.request.query_params.get('name'):
            queryset = queryset.filter(name__icontains=self.request.query_params['name'])

        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
