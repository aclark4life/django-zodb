from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.client import BaseDatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation
from django.db.backends.base.features import BaseDatabaseFeatures
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.exceptions import DatabaseError


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'zodb'
    display_name = 'ZODB'
    connection = None
    client_class = BaseDatabaseClient
    creation_class = BaseDatabaseCreation
    features_class = BaseDatabaseFeatures
    introspection_class = BaseDatabaseIntrospection
    ops_class = BaseDatabaseOperations

    class Database(object):
        DataError = DatabaseError

    Database = Database
