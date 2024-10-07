# django_zodb/management/commands/dumpzodb.py

from django.core.management.base import BaseCommand
from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction
import BTrees


class Command(BaseCommand):
    help = "Dump all objects from the ZODB"

    def handle(self, *args, **kwargs):
        storage = FileStorage("Data.fs")
        db = DB(storage)
        connection = db.open()
        root = connection.root()
        self.walk_zodb(root)
        transaction.abort()
        connection.close()
        db.close()

    def walk_zodb(self, obj, path="", depth=0):
        indent = "  " * depth
        print(f"{indent}{path}: {obj}")
        if isinstance(obj, dict) or isinstance(
            obj,
            (BTrees.OOBTree.OOBTree, BTrees.IOBTree.IOBTree, BTrees.LOBTree.LOBTree),
        ):
            for key, value in obj.items():
                self.walk_zodb(value, f"{path}/{key}", depth + 1)
        elif isinstance(obj, list):
            for index, value in enumerate(obj):
                self.walk_zodb(value, f"{path}/{index}", depth + 1)
        elif hasattr(obj, "__dict__"):
            for key, value in obj.__dict__.items():
                self.walk_zodb(value, f"{path}/{key}", depth + 1)
        elif hasattr(obj, "__slots__"):
            for key in obj.__slots__:
                self.walk_zodb(getattr(obj, key), f"{path}/{key}", depth + 1)
