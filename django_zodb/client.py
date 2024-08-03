# django_zodb/client.py
from django.db.backends.base.client import BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    def runshell(self):
        # Implement shell command
        pass
