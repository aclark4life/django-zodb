import transaction


class ZODBCursor:
    def __init__(self, connection):
        self.connection = connection
        self.lastrowid = None  # Initialize lastrowid attribute
        self.rowcount = -1  # Initialize rowcount attribute

    def execute(self, sql, params=None):
        # Convert sql to string if it's not already
        sql = str(sql)
        # Implement interaction with ZODB here
        print(f"Executing SQL: {sql} with params: {params}")
        # Example logic to handle table creation and data insertion
        if sql.startswith("CREATE TABLE"):
            table_name = sql.split()[2].strip('"')
            if table_name not in self.connection.root:
                self.connection.root[table_name] = PersistentMapping()
                transaction.commit()
                self.rowcount = 0
            else:
                print(f"Table {table_name} already exists")
        elif sql.startswith("INSERT INTO"):
            table_name = sql.split()[2].strip('"')
            table = self.connection.root.get(table_name)
            if table is not None:
                row_id = len(table) + 1
                table[row_id] = params
                transaction.commit()
                self.lastrowid = row_id
                self.rowcount = 1
            else:
                raise DatabaseError(f"Table {table_name} does not exist")
        else:
            print("Unsupported SQL command")

    def fetchall(self):
        # Implement fetching data from ZODB here
        return []

    def fetchmany(self, size=None):
        # Implement fetching data from ZODB here
        return []

    def close(self):
        print("Closing cursor")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
