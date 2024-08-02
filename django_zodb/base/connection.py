from ZODB import DB
from ZODB.FileStorage import FileStorage

class ZODBConnection:
    def __init__(self, path):
        self.path = path
        self.storage = None
        self.db = None
        self.connection = None

    def connect(self):
        self.storage = FileStorage(self.path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        return self.connection

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
