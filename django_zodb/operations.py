# django_zodb/operations.py
from django.db.backends.base.operations import BaseDatabaseOperations

class DatabaseOperations(BaseDatabaseOperations):
    def quote_name(self, name):
        # Quote a database name
        pass

    def sql_flush(self, style, tables, sequences, allow_cascade=False):
        # Return SQL statements to flush the database
        pass
