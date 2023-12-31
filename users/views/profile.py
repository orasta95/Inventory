from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics,status

from ..serializers import UserSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "delete", "patch"]

    def get_object(self):
        return self.request.user
 
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
