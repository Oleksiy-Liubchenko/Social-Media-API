from rest_framework import serializers
from post.models import Post, Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ("name",)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "content",
            "created_at",
            "hashtag",
        )
        read_only_fields = ("user",)


class PostListSerializer(PostSerializer):
    hashtag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
