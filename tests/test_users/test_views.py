import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.factories import UserFactory
from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_user_list_get_without_credentials(api_client):
    url = reverse('Users')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_user_list_post(api_client):
    url = reverse('Users')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    user = User.objects.get(username='testuser')
    assert user.email == 'test@example.com'
    assert user.username == 'testuser'


@pytest.mark.django_db
def test_user_detail_get(api_client):
    user = UserFactory()
    url = reverse('User', args=[user.id])
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('username') == user.username
    assert response.data.get('email') == user.email


@pytest.mark.django_db
def test_user_match_post(api_client):
    follower = UserFactory()
    user = UserFactory()
    url = reverse('follow_user', args=[follower.id, user.id])
    api_client.force_authenticate(user=follower)
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    assert follower.following.filter(id=user.id).exists()


@pytest.mark.django_db
def test_user_match_post_same_user(api_client):
    user = UserFactory()
    url = reverse('follow_user', args=[user.id, user.id])
    api_client.force_authenticate(user=user)
    response = api_client.post(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data.get('error') == "You cannot follow yourself."


@pytest.mark.django_db
def test_user_match_post_another_user(api_client):
    follower = UserFactory()
    user = UserFactory()
    another = UserFactory()
    url = reverse('follow_user', args=[follower.id, user.id])
    api_client.force_authenticate(user=another)
    response = api_client.post(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
