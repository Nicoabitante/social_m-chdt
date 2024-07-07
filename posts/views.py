import datetime

from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Comment
from posts.serializers import PostSerializer, PostDetailSerializer, CommentSerializer


class PostListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.all()
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        author_id = self.request.query_params.get('author_id')
        if author_id:
            queryset = queryset.filter(author__id=author_id)

        if from_date and to_date:
            try:
                from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d').date()
                to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d').date()
            except ValueError:
                pass
            else:
                queryset = queryset.filter(Q(created_at__gte=from_date), Q(created_at__lte=to_date))

        return queryset


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated]


class CommentsListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['pk'])
