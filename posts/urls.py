from django.urls import path

from posts.views import PostListCreate, PostDetailView, CommentsListCreateView

urlpatterns = [
    path('', PostListCreate.as_view(), name='Posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='Post'),
    path('<int:pk>/comments/', CommentsListCreateView.as_view(), name='Comments')
]
