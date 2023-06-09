from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserProfile
from user.permissions import IsOwnerOrReadOnly
from user.serializers import (
    UserSerializer,
    UserProfileListSerializer,
    UserProfileDetailSerializer,
)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MyUserProfile(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        username = self.request.query_params.get("username")
        bio = self.request.query_params.get("bio")

        if username:
            queryset = queryset.filter(username__icontains=username)

        if bio:
            queryset = queryset.filter(bio__icontains=bio)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserProfileDetailSerializer
        return UserProfileListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
