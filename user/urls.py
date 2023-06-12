from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from user import views
from user.views import RegisterView, UserProfileViewSet

router = routers.DefaultRouter()
router.register("profiles", UserProfileViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="sign_up"),
    path("me/", views.MyUserProfile.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "<int:pk>/follow_toggle/",
        UserProfileViewSet.as_view({"post": "follow_toggle"}),
        name="user-profiles-follow-toggle",
    ),
    path("", include(router.urls)),
]

app_name = "user"
