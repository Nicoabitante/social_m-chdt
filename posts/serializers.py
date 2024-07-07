from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['content', 'author']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['author', 'content', 'created_at', 'comments']


class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'comments']

    def get_comments(self, obj):
        comments = obj.comments.all()[:3]
        return CommentSerializer(comments, many=True).data
