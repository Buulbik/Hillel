from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response

from apps.api.blog.serializers import ArticleReadSerializer, ArticleWriteSerializer
from apps.blog.models import Article, Tag


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ArticleReadSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ArticleWriteSerializer
        return self.serializer_class

    @staticmethod
    def check_tags(tags):
        tags_list = []
        for item in tags:
            tag = Tag.objects.filter(name=item).first()
            if not tag:
                tag = Tag.objects.create(name=item)
            tags_list.append(tag)
        return tags_list

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tags = serializer.validated_data.get('tags')

        article = serializer.save(user=self.request.user, tags=self.check_tags(tags))
        read_serializer = self.serializer_class(article, context={'request': request})
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Article.objects.all()
        if self.request.query_params.get('category'):
            queryset = queryset.filter(category_id=self.request.query_params['category'])
        if self.request.query_params.get('user'):
            queryset = queryset.filter(user=self.request.query_params['user'])

        return queryset
