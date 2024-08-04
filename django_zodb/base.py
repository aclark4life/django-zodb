from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.features import BaseDatabaseFeatures
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db import (
    DatabaseError,
    InterfaceError,
    DataError,
    OperationalError,
    IntegrityError,
    InternalError,
    ProgrammingError,
    NotSupportedError,
)

# Dummy Features
class DummyDatabaseFeatures(BaseDatabaseFeatures):
    def __init__(self, connection):
        super().__init__(connection)
        self.can_rollback_ddl = True

# Dummy Cursor and Connection
class DummyCursor:
    def __init__(self):
        self.lastrowid = None  # Add the lastrowid attribute
        self.rowcount = 0  # Add the rowcount attribute

    def execute(self, sql, params=None):
        print(f"Executing SQL: {sql} with params: {params}")
        self.lastrowid = 1  # Simulate an auto-increment ID
        self.rowcount = 1  # Simulate a row count

    def fetchall(self):
        return []

    def fetchmany(self, size=None):
        return []

    def close(self):
        print("Closing cursor")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class DummyConnection:
    alias = 'default'  # Add the alias attribute
    vendor = 'dummy'  # Add the vendor attribute

    def __init__(self):
        self.features = DummyDatabaseFeatures(self)  # Initialize features with self
        self.ops = DatabaseOperations(self)  # Initialize ops with self
        self.data_types = {  # Add the data_types attribute
            'AutoField': 'integer',
            'BigAutoField': 'bigint',
            'BinaryField': 'blob',
            'BooleanField': 'bool',
            'CharField': 'varchar',
            'DateField': 'date',
            'DateTimeField': 'timestamp',
            'DecimalField': 'decimal',
            'DurationField': 'interval',
            'FileField': 'varchar',
            'FilePathField': 'varchar',
            'FloatField': 'real',
            'IntegerField': 'integer',
            'BigIntegerField': 'bigint',
            'IPAddressField': 'char(15)',
            'GenericIPAddressField': 'char(39)',
            'NullBooleanField': 'bool',
            'OneToOneField': 'integer',
            'PositiveIntegerField': 'integer',
            'PositiveSmallIntegerField': 'smallint',
            'SlugField': 'varchar',
            'SmallIntegerField': 'smallint',
            'TextField': 'text',
            'TimeField': 'time',
            'UUIDField': 'char(32)',
        }
        self.data_type_check_constraints = {  # Add the data_type_check_constraints attribute
            'PositiveIntegerField': '%(column)s >= 0',
            'PositiveSmallIntegerField': '%(column)s >= 0',
        }
        self.data_types_suffix = {  # Add the data_types_suffix attribute
            'AutoField': '',
            'BigAutoField': '',
            'BinaryField': '',
            'BooleanField': '',
            'CharField': '',
            'DateField': '',
            'DateTimeField': '',
            'DecimalField': '',
            'DurationField': '',
            'FileField': '',
            'FilePathField': '',
            'FloatField': '',
            'IntegerField': '',
            'BigIntegerField': '',
            'IPAddressField': '',
            'GenericIPAddressField': '',
            'NullBooleanField': '',
            'OneToOneField': '',
            'PositiveIntegerField': '',
            'PositiveSmallIntegerField': '',
            'SlugField': '',
            'SmallIntegerField': '',
            'TextField': '',
            'TimeField': '',
            'UUIDField': '',
        }

    def cursor(self):
        return DummyCursor()

    def commit(self):
        print("Committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def close(self):
        print("Closing connection")

# Dummy DatabaseClient
class DatabaseClient:
    def __init__(self, connection):
        self.connection = connection

    def runshell(self):
        print("Running shell")

# Dummy DatabaseCreation
class DatabaseCreation:
    def __init__(self, connection):
        self.connection = connection

    def create_test_db(self, *args, **kwargs):
        print("Creating test database")

    def destroy_test_db(self, *args, **kwargs):
        print("Destroying test database")

# Dummy DatabaseSchemaEditor
class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    atomic_migration = False  # Add the atomic_migration attribute
    deferred_sql = []  # Add the deferred_sql attribute

    def __init__(self, connection, collect_sql=False, *args, **kwargs):
        super().__init__(connection, collect_sql, *args, **kwargs)
        self.connection = connection
        self.collect_sql = collect_sql
        self.collected_sql = []

    def execute(self, sql, params=()):
        if self.collect_sql:
            self.collected_sql.append(sql)
        else:
            print(f"Executing SQL: {sql}")

    def create_model(self, model):
        sql = f"CREATE TABLE {model._meta.db_table} (...);"
        self.execute(sql)

    def delete_model(self, model):
        sql = f"DROP TABLE {model._meta.db_table};"
        self.execute(sql)

    def alter_unique_together(self, model, old_unique_together, new_unique_together):
        print(f"Altering unique_together for {model._meta.db_table} from {old_unique_together} to {new_unique_together}")

    def alter_field(self, model, old_field, new_field, strict=False):
        print(f"Altering field {old_field.name} to {new_field.name} in model {model._meta.db_table}")

    def remove_field(self, model, field):
        print(f"Removing field {field.name} from model {model._meta.db_table}")

    def add_constraint(self, model, constraint):
        print(f"Adding constraint {constraint.name} to model {model._meta.db_table}")

    # Add other schema operations as needed

# Dummy DatabaseIntrospection
class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        return []

    def get_table_description(self, cursor, table_name):
        return []

    def get_relations(self, cursor, table_name):
        return {}

    def get_indexes(self, cursor, table_name):
        return {}

    def get_constraints(self, cursor, table_name):
        return {}

# Dummy DatabaseOperations
class DatabaseOperations(BaseDatabaseOperations):
    def __init__(self, connection):
        super().__init__(connection)

    def quote_name(self, name):
        return f'"{name}"'

# DatabaseWrapper
class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'dummy'
    display_name = 'DummyDB'
    client_class = DatabaseClient  # Set the client_class attribute
    creation_class = DatabaseCreation  # Set the creation_class attribute
    schema_editor_class = DatabaseSchemaEditor  # Set the schema_editor_class attribute
    introspection_class = DatabaseIntrospection  # Set the introspection_class attribute
    ops_class = DatabaseOperations  # Set the ops_class attribute
    features_class = DummyDatabaseFeatures  # Set the features_class attribute

    operators = {
        'exact': '= %s',
        'iexact': 'ILIKE %s',
        'contains': 'LIKE %s',
        'icontains': 'ILIKE %s',
        'regex': '~ %s',
        'iregex': '~* %s',
        'gt': '> %s',
        'gte': '>= %s',
        'lt': '< %s',
        'lte': '<= %s',
        'startswith': 'LIKE %s',
        'istartswith': 'ILIKE %s',
        'endswith': 'LIKE %s',
        'iendswith': 'ILIKE %s',
    }

    class Database:
        Error = DatabaseError
        InterfaceError = InterfaceError
        DatabaseError = DatabaseError
        DataError = DataError
        OperationalError = OperationalError
        IntegrityError = IntegrityError
        InternalError = InternalError
        ProgrammingError = ProgrammingError
        NotSupportedError = NotSupportedError

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection = None
        self._in_connect = False

    def get_connection_params(self):
        return {}

    def get_new_connection(self, conn_params):
        return DummyConnection()

    def init_connection_state(self):
        pass

    def create_cursor(self, name=None):
        return self.connection.cursor()

    def _set_autocommit(self, autocommit):
        print(f"Setting autocommit to {autocommit}")

    def schema_editor(self, *args, **kwargs):
        return self.schema_editor_class(self.connection, *args, **kwargs)

    def _commit(self):
        self.connection.commit()

    def _rollback(self):
        self.connection.rollback()

    def _close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
