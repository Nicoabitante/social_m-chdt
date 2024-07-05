from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserMatch(APIView):
    def post(self, request, follower_id, user_id):
        follower = generics.get_object_or_404(User, id=follower_id)
        user = generics.get_object_or_404(User, id=user_id)
        if request.user.id != follower_id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if user == follower:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        follower.following.add(user)
        return Response({'status': 'Following user successfully.'}, status=status.HTTP_200_OK)
