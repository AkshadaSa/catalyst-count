import environ
from django.test import TestCase

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

class SimpleTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_db_env_variables(self):
        # Example test for checking environment variables
        self.assertEqual(env('DB_NAME', default='default_value'), 'catalyst_db')
        self.assertEqual(env('DB_USER', default='default_value'), 'catalyst_user')
