import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from posts.factories import UserFactory, PostFactory, CommentFactory
from posts.models import Post, Comment


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_post_list_create_get(api_client):
    url = reverse('Posts')
    user = UserFactory()
    api_client.force_authenticate(user=user)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_list_create_post(api_client):
    url = reverse('Posts')
    user = UserFactory()
    api_client.force_authenticate(user=user)

    data = {
        'content': 'Test post content'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.filter(author=user, content='Test post content').exists()


@pytest.mark.django_db
def test_post_detail_view(api_client):
    post = PostFactory()
    url = reverse('Post', args=[post.id])
    user = post.author
    api_client.force_authenticate(user=user)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_comments_list_create_view_get(api_client):
    post = PostFactory()
    url = reverse('Comments', args=[post.id])
    user = UserFactory()
    api_client.force_authenticate(user=user)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_comments_list_create_view_get_without_cred(api_client):
    post = PostFactory()
    url = reverse('Comments', args=[post.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_comments_list_create_view_post(api_client):
    post = PostFactory()
    url = reverse('Comments', args=[post.id])
    user = UserFactory()
    api_client.force_authenticate(user=user)

    data = {
        'content': 'Test comment content'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Comment.objects.filter(author=user, post=post, content='Test comment content').exists()
