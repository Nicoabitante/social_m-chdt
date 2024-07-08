import factory
from django.core.management.base import BaseCommand
from users.factories import UserFactory
from posts.factories import PostFactory, CommentFactory


class Command(BaseCommand):
    help = 'Populate the database with random data'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, help='Number of users to create')
        parser.add_argument('--posts', type=int, help='Number of posts to create')
        parser.add_argument('--comments', type=int, help='Number of comments to create')

    def handle(self, *args, **kwargs):
        num_users = kwargs.get('users') or 10
        num_posts = kwargs.get('posts') or 50
        num_comments = kwargs.get('comments') or 200

        self.stdout.write(self.style.NOTICE(f'Creating {num_users} users...'))
        users = UserFactory.create_batch(num_users)

        self.stdout.write(self.style.NOTICE(f'Creating {num_posts} posts...'))
        posts = PostFactory.create_batch(num_posts, author=factory.Iterator(users))

        self.stdout.write(self.style.NOTICE(f'Creating {num_comments} comments...'))
        CommentFactory.create_batch(num_comments, author=factory.Iterator(users), post=factory.Iterator(posts))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))