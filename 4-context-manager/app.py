# lets import the custom file open


# app.py

from utils.contextManager import CustomFileOpen, CustomConnection

with CustomFileOpen("file.txt", "w") as file: 
    file.write("Hello there !")




with CustomConnection('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(name VARCHAR(40), author VARCHAR(30));")
    cursor.execute("INSERT INTO books (name, author) VALUES ('Faults in our stars','Ujjwal')")
    cursor.execute("SELECT name, author FROM books")

    book_list = cursor.fetchall() 


print(book_list)

