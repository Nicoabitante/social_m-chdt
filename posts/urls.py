from django.urls import path

from posts.views import PostListCreate, PostDetailView, CommentsListCreateView

urlpatterns = [
    path('', PostListCreate.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('<int:pk>/comments/', CommentsListCreateView.as_view())
]
