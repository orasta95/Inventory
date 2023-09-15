from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..serializers import ProductSerializer, ProductShortSerializer, ProductCreateSerializer
from ..models import Product


class ProductApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    #permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return ProductShortSerializer
        if (self.action == "create"):
            return ProductCreateSerializer
        if (self.action == "patch"):
            return ProductCreateSerializer
        return ProductSerializer
