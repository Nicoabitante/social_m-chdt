from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from posts.serializers import PostSerializer, CommentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    following = UserSerializer(many=True, read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'followers', 'following', 'posts', 'comments']
