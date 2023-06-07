from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post import views


router = DefaultRouter()
router.register("post", views.PostViewSet, basename="post")
router.register("hashtag", views.HashtagViewSet, basename="hashtag")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "social"
