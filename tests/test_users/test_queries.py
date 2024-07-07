import pytest

from posts.factories import PostFactory, CommentFactory
from posts.models import Post, Comment
from users.factories import UserFactory
from users.models import User


@pytest.mark.django_db
def test_create_user():
    user = UserFactory(username='testuser', email='test@example.com')
    assert User.objects.filter(username='testuser').exists()
    assert User.objects.filter(email='test@example.com').exists()


@pytest.mark.django_db
def test_create_post():
    user = UserFactory()
    post = PostFactory(author=user, content='Test post content')
    assert Post.objects.filter(author=user, content='Test post content').exists()


@pytest.mark.django_db
def test_create_comment():
    user = UserFactory()
    post = PostFactory(author=user)
    comment = CommentFactory(author=user, post=post, content='Test comment content')
    assert Comment.objects.filter(author=user, post=post, content='Test comment content').exists()


@pytest.mark.django_db
def test_post_related_comments():
    post = PostFactory()
    comments = CommentFactory.create_batch(5, post=post)
    assert Comment.objects.filter(post=post).count() == 5


@pytest.mark.django_db
def test_user_posts():
    user = UserFactory()
    posts = PostFactory.create_batch(3, author=user)
    assert Post.objects.filter(author=user).count() == 3


@pytest.mark.django_db
def test_user_comments():
    user = UserFactory()
    post = PostFactory()
    comments = CommentFactory.create_batch(4, author=user, post=post)
    assert Comment.objects.filter(author=user, post=post).count() == 4
