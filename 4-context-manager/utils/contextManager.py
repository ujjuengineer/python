import sqlite3

class CustomFileOpen: 
    """context manager for managing files"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file # return the opened file pointer
        
    def __exit__(self, exc_type, exc, tb):
        self.file.close()


class CustomConnection:
    """context manager for db connection handling"""
    def __init__(self, database):
        self.db = database

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        return self.connection

    def __exit__(self, exc_type, exc, tb):
        self.connection.commit()
        self.connection.close()

# lets built the context manager for database management

# import sqlite3

# conn = sqlite3.connect("company.db")

# cursor = conn.cursor()
# cursor.execute('CREATE TABLE employees (name VARCHAR(50), role VARCHAR(50));')
# conn.commit()

# conn.close()


# if you notice while working with sqlite we always have to built a connection and then close that connection
# so we can do this using context manager



