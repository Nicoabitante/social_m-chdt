from django.urls import path

from posts.views import PostListCreate, PostDetailView

urlpatterns = [
    path('', PostListCreate.as_view()),
    path('<int:pk>/', PostDetailView.as_view())
]
