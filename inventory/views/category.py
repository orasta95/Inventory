from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..serializers import CategorySerializer, CategoryShortSerializer, CategoryCreateSerializer
from ..models import Category


class CategoryApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    #permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return CategoryShortSerializer
        if (self.action == "create"):
            return CategoryCreateSerializer
        if (self.action == "patch"):
            return CategoryCreateSerializer
        return CategorySerializer
