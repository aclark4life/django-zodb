"""
Dummy database backend for Django.

Django uses this if the database ENGINE setting is empty (None or empty string).

Each of these API functions, except connection.close(), raise
ImproperlyConfigured.
"""

from django.core.exceptions import ImproperlyConfigured
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.client import BaseDatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.dummy.features import DummyDatabaseFeatures
from django.db.backends.signals import connection_created
from ZODB import FileStorage, DB

# from .wrapper import DatabaseWrapper


def complain(*args, **kwargs):
    raise ImproperlyConfigured(
        "settings.DATABASES is improperly configured. "
        "Please supply the ENGINE value. Check "
        "settings documentation for more details."
    )


def ignore(*args, **kwargs):
    pass


class DatabaseOperations(BaseDatabaseOperations):
    quote_name = complain


class DatabaseClient(BaseDatabaseClient):
    runshell = complain


class DatabaseCreation(BaseDatabaseCreation):
    create_test_db = ignore
    destroy_test_db = ignore


class DatabaseIntrospection(BaseDatabaseIntrospection):
    get_table_list = complain
    get_table_description = complain
    get_relations = complain
    get_indexes = complain


# class DatabaseWrapper(BaseDatabaseWrapper):
#     operators = {}
#     # Override the base class implementations with null
#     # implementations. Anything that tries to actually
#     # do something raises complain; anything that tries
#     # to rollback or undo something raises ignore.
#     _cursor = complain
#     ensure_connection = complain
#     _commit = complain
#     _rollback = ignore
#     _close = ignore
#     _savepoint = ignore
#     _savepoint_commit = complain
#     _savepoint_rollback = ignore
#     _set_autocommit = complain
#     # Classes instantiated in __init__().
#     client_class = DatabaseClient
#     creation_class = DatabaseCreation
#     features_class = DummyDatabaseFeatures
#     introspection_class = DatabaseIntrospection
#     ops_class = DatabaseOperations
# 
#     def is_usable(self):
#         return True


class DatabaseWrapper(BaseDatabaseWrapper):
    operators = {}

    vendor = 'zodb'
    display_name = 'ZODB'

    # SchemaEditorClass = DatabaseSchemaEditor
    client_class = DatabaseClient
    introspection_class = DatabaseIntrospection
    # features_class = DatabaseFeatures
    features_class = DummyDatabaseFeatures
    ops_class = DatabaseOperations

    _cursor = complain
    ensure_connection = complain
    _commit = complain
    _rollback = ignore
    _close = ignore
    _savepoint = ignore
    _savepoint_commit = complain
    _savepoint_rollback = ignore
    _set_autocommit = complain
    # Classes instantiated in __init__().
    client_class = DatabaseClient
    creation_class = DatabaseCreation

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connected = False
        del self.connection

    def get_connection_params(self):
        return {
            'path': self.settings_dict.get('NAME'),
        }

    def get_new_connection(self, conn_params):
        storage = FileStorage.FileStorage('Data.fs')
        db = DB(storage)
        return db.open()

    def init_connection_state(self):
        pass

    def create_cursor(self, name=None):
        return self.connection.root()

    def close(self):
        if self.zodb_conn is not None:
            self.zodb_conn.close()
            self.zodb_conn = None

    def _commit(self):
        transaction.commit()

    def _rollback(self):
        transaction.abort()

    def _savepoint(self, sid):
        return transaction.savepoint()

    def _savepoint_rollback(self, sid):
        sid.rollback()

    def _savepoint_commit(self, sid):
        sid.commit()

    def _set_autocommit(self, autocommit):
        pass

    # Via https://github.com/aclark4life/django-mongodb
    def __getattr__(self, attr):
        """
        Connect to the database the first time `connection` or `database` are
        accessed.
        """
        if attr in ["connection", "database"]:
            assert not self.connected
            self._connect()
            return getattr(self, attr)
        raise AttributeError(attr)

    def _connect(self):
        settings_dict = self.settings_dict
        
        options = settings_dict["OPTIONS"]
        # TODO: review and document OPERATIONS: https://github.com/mongodb-labs/django-mongodb/issues/6
        self.operation_flags = options.pop("OPERATIONS", {})
        if not any(k in ["save", "delete", "update"] for k in self.operation_flags):
            # Flags apply to all operations.
            flags = self.operation_flags
            self.operation_flags = {"save": flags, "delete": flags, "update": flags}
        
        self.connection = self.get_new_connection({})

        db_name = settings_dict["NAME"]
        if db_name:
            self.database = self.connection[db_name]
        
        user = settings_dict["USER"]
        password = settings_dict["PASSWORD"]
        if user and password and not self.database.authenticate(user, password):
            raise ImproperlyConfigured("Invalid username or password.")

        self.connected = True
        connection_created.send(sender=self.__class__, connection=self)

