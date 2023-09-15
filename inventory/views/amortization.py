from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..serializers import AmortizationSerializer, AmortizationShortSerializer, AmortizationCreateSerializer
from ..models import Amortization


class AmortizationApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    #permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Amortization.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return AmortizationShortSerializer
        if (self.action == "create"):
            return AmortizationCreateSerializer
        if (self.action == "patch"):
            return AmortizationCreateSerializer
        return AmortizationSerializer
