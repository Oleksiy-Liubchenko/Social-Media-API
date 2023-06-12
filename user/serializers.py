from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "is_staff")
        read_only_fields = ("is_staff",)
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, set the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user


class UserProfileListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    follow_status = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "user",
            "email",
            "username",
            "bio",
            "profile_photo",
            "follow_status",
        )
        read_only_fields = ("id", "user")

    def get_follow_status(self, obj):
        """show you is you following this user profile or not"""
        user = self.context["request"].user
        if obj.followers.filter(pk=user.pk).exists():
            return "following"
        return "not following"


class UserProfileDetailSerializer(UserProfileListSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "user",
            "username",
            "bio",
            "profile_photo",
            "followings",
            "followers",
        )
