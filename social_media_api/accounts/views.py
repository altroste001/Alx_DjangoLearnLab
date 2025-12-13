from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, UserSerializer


CustomUser = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"detail": "User followed"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": "User unfollowed"}, status=status.HTTP_200_OK)
