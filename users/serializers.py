from rest_framework import serializers

from posts.serializers import PostSerializer, CommentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserDetailSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    following = UserSerializer(many=True, read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'followers', 'following', 'posts', 'comments']
