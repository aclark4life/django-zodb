class FriendlyRoot:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        if hasattr(self.root, "keys"):
            return f"<FriendlyRoot with tables: {list(self.root.keys())}>"
        else:
            return "<FriendlyRoot>"

    def list_tables(self):
        if hasattr(self.root, "_root"):
            return list(self.root._root.keys())
        else:
            return []

    def __getattr__(self, name):
        return getattr(self.root, name)
