from curses import curs_set
import sqlite3
from venv import create

# from utils.database_connection import DatabaseConnection

# Book = Tuple[int, str, str, int]


def create_book_table() -> None:
    connection = sqlite3.connect("book.db")
    cursor = connection.cursor()
    
    # Added DEFAULT 0 to the read column
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            name TEXT, 
            author TEXT, 
            read INTEGER DEFAULT 0
        );
    """)
    
    connection.commit()
    connection.close()



def get_all_books(): 
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, author, read FROM books")

    book_list = cursor.fetchall() # this gives list of tuples
    conn.close()

    return book_list


def insert_book(name: str, author: str) -> None:

    create_book_table() # this will create the table if table doesn't exist

    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books (name, author) VALUES (?, ?)", (name, author))
    
    conn.commit()
    conn.close()

def mark_book_as_read(name: str) -> None:
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE books SET read=? WHERE name =?", (1,name))

    conn.commit()
    conn.close()


def delete_book(name: str) -> None:
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE name=?",(name,))
    conn.close()