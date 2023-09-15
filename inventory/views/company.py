from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..serializers import CompanySerializer, CompanyShortSerializer, CompanyCreateSerializer
from ..models import Company


class CompanyApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    #permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return CompanyShortSerializer
        if (self.action == "create"):
            return CompanyCreateSerializer
        if (self.action == "patch"):
            return CompanyCreateSerializer
        return CompanySerializer
