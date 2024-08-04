class FriendlyRoot:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        if hasattr(self.root, "_root"):
            return f"<ZODB with tables: {list(self.root._root)}>"
        else:
            return "<ZODB with no tables"

    def tables(self):
        if hasattr(self.root, "_root"):
            return list(self.root._root)
        else:
            return []

    def __getattr__(self, name):
        return getattr(self.root, name)
