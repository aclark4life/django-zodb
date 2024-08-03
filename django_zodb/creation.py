# django_zodb/creation.py
from django.db.backends.base.creation import BaseDatabaseCreation

class DatabaseCreation(BaseDatabaseCreation):
    def create_test_db(self, *args, **kwargs):
        # Create test database
        pass

    def destroy_test_db(self, *args, **kwargs):
        # Destroy test database
        pass