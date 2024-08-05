class ZODBRoot:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        if hasattr(self.root, "_root"):
            return f"<ZODB with tables: {list(self.root._root)}>"

    def __getattr__(self, name):
        return getattr(self.root, name)
