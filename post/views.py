from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from post.models import Post, Hashtag
from post.permissions import IsOwnerOrReadOnly
from post.serializers import PostSerializer, HashtagSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        followings = self.request.user.userprofile.followings.all()
        queryset = self.queryset.filter(
            user__in=list(followings) + [self.request.user.id]
        )

        user = self.request.query_params.get("user")
        hashtag = self.request.query_params.get("hashtag")

        if user:
            queryset = queryset.filter(user__in=user)

        if hashtag:
            queryset = queryset.filter(hashtag__name__icontains=hashtag)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PostListSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "user",
                type=int,
                description="Filtering posts by user id ex. ?user=1",
            ),
            OpenApiParameter(
                "hashtag",
                type=str,
                description="Filtering by hashtag (write some symbol that "
                "contains in username). ex. ?hashtag=te",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
