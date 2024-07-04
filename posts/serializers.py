from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']


class PostSerializers(serializers.ModelSerializer):
    comments = CommentSerializer(source='comments', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['content', 'created_at', 'comments']
