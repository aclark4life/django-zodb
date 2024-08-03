"""
ZODB backend
"""

from django.core.exceptions import ImproperlyConfigured
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.client import BaseDatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.dummy.features import DummyDatabaseFeatures
from django.db.backends.signals import connection_created
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from ZODB import FileStorage, DB


class ZODBCursor:
    def execute(self, command, *args):
        if command == 'ADD':
            app_label, migration_name, applied = args
            record = MigrationRecord(app_label, migration_name, applied)
            self.migrations[(app_label, migration_name)] = record
            transaction.commit()
        elif command == 'GET':
            app_label, migration_name = args
            return self.migrations.get((app_label, migration_name))
        elif command == 'LIST':
            return list(self.migrations.values())
        else:
            raise ValueError("Unknown command")

    def __iter__(self):
        self._iter = iter(self.migrations.items())
        return self

    def __next__(self):
        return next(self._iter)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class ZODBConnection:
    def __init__(self, db_path='Data.fs'):
        self.db_path = db_path
        self.storage = None
        self.db = None
        self.connection = None

    def __enter__(self):
        self.storage = ZODB.FileStorage.FileStorage(self.db_path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
        if self.db is not None:
            self.db.close()
            self.db = None
        if self.storage is not None:
            self.storage.close()
            self.storage = None

    def cursor(self):
        return ZODBCursor(self.root)


def complain(*args, **kwargs):
    print(args, kwargs)
    raise ImproperlyConfigured(
        "settings.DATABASES is improperly configured. "
        "Please supply the ENGINE value. Check "
        "settings documentation for more details."
    )


def ignore(*args, **kwargs):
    pass


class DatabaseOperations(BaseDatabaseOperations):
    def quote_name(self, name):
        if name.startswith('"') and name.endswith('"'):
            return name  # Quoting once is enough.
        return name


class DatabaseClient(BaseDatabaseClient):
    runshell = complain


class DatabaseCreation(BaseDatabaseCreation):
    create_test_db = ignore
    destroy_test_db = ignore


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def table_names(self, cursor=None, include_views=False):
        # return [x["name"] for x in self.connection.database.list_collections()]
        return []


class DatabaseWrapper(BaseDatabaseWrapper):
    operators = {}

    vendor = 'zodb'
    display_name = 'ZODB'

    SchemaEditorClass = BaseDatabaseSchemaEditor
    client_class = DatabaseClient
    introspection_class = DatabaseIntrospection
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
        self.connection = ZODBConnection()
        return self.connection

    def init_connection_state(self):
        pass

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

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

    @staticmethod
    def get_autocommit():
        return False

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
