from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates multiple users for testing purposes'

    def handle(self, *args, **kwargs):
        for i in range(15):  # Adjust the range to create more users
            User.objects.create_user(username=f'user{i}', password='password', email=f'user{i}@example.com')
        self.stdout.write(self.style.SUCCESS('Successfully created 15 users'))
