# django_zodb/introspection.py
from django.db.backends.base.introspection import BaseDatabaseIntrospection

class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        # Return a list of table names
        pass

    def get_table_description(self, cursor, table_name):
        # Return a description of the table
        pass

    def get_relations(self, cursor, table_name):
        # Return a dictionary of relations
        pass

    def get_indexes(self, cursor, table_name):
        # Return a dictionary of indexes
        pass
