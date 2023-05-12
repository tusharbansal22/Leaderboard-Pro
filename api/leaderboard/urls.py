"""leaderboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import  Group
from rest_framework import serializers, viewsets, routers, permissions
from leaderboard import views

from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-usernames")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)


urlpatterns = [
    path("", views.api_root),
    path('api/',include('leaderboard.api.urls')),
    path(
        "codeforces/",
        views.CodeforcesLeaderboard.as_view(),
        name="codeforces-leaderboard",
    ),
    path(
        "leetcode/",
        views.LeetcodeLeaderboard.as_view(),
        name="leetcode-leaderboard",
    ),
    # path(
    #     "appuser/",
    #     views.AppUsers.as_view(),
    #     name="app-user",
    # ),
    path(
        "codeforces/<int:pk>",
        views.codeforcesUserAPI.as_view(),
        name="codeforces-user-details",
    ),
    path(
        "codechef/",
        views.CodechefLeaderboard.as_view(),
        name="codechef-leaderboard",
    ),
    path("github/", views.GithubUserAPI.as_view(), name="github-leaderboard"),
    path(
        "openlake/",
        views.GithubOrganisationAPI.as_view(),
        name="openlake-leaderboard",
    ),
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls
