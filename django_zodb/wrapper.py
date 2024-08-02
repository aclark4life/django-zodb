from django.db.backends.base.base import BaseDatabaseWrapper
from .operations import DatabaseOperations
from .client import DatabaseClient
from .schema import DatabaseSchemaEditor
from .introspection import DatabaseIntrospection
from .features import DatabaseFeatures
from .connection import ZODBConnection
import transaction

class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'zodb'
    display_name = 'ZODB'

    SchemaEditorClass = DatabaseSchemaEditor
    client_class = DatabaseClient
    introspection_class = DatabaseIntrospection
    features_class = DatabaseFeatures
    ops_class = DatabaseOperations

    def get_connection_params(self):
        return {
            'path': self.settings_dict.get('NAME'),
        }

    def get_new_connection(self, conn_params):
        self.zodb_conn = ZODBConnection(conn_params['path'])
        return self.zodb_conn.connect()

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
