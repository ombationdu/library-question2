import mysql.connector

class Book:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="Library"
        )
        self.cursor = self.db_connection.cursor()

    def add_book(self, title, author, quantity):
        try:
            sql = "INSERT INTO bookRecord (Title, Author, Quantity, Available) VALUES (%s, %s, %s, %s)"
            book_data = (title, author, quantity, quantity)
            self.cursor.execute(sql, book_data)
            self.db_connection.commit()
            print("Book added successfully.")
        except mysql.connector.Error as error:
            print("Error adding book:", error)

    def update_book(self, bno, title, author, quantity):
        try:
            sql = "UPDATE bookRecord SET Title=%s, Author=%s, Quantity=%s, Available=%s WHERE Bno=%s"
            book_data = (title, author, quantity, quantity, bno)
            self.cursor.execute(sql, book_data)
            self.db_connection.commit()
            print("Book updated successfully.")
        except mysql.connector.Error as error:
            print("Error updating book:", error)

    def delete_book(self, bno):
        try:
            sql = "DELETE FROM bookRecord WHERE Bno=%s"
            self.cursor.execute(sql, (bno,))
            self.db_connection.commit()
            print("Book deleted successfully.")
        except mysql.connector.Error as error:
            print("Error deleting book:", error)

    def display_books(self):
        try:
            self.cursor.execute("SELECT * FROM bookRecord")
            books = self.cursor.fetchall()
            if books:
                print("======= Books in Library =======")
                print("Bno\tTitle\tAuthor\tQuantity\tAvailable")
                for book in books:
                    print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}\t\t{book[4]}")
                print("================================")
            else:
                print("No books available in the library.")
        except mysql.connector.Error as error:
            print("Error displaying books:", error)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.db_connection:
            self.db_connection.close()


if __name__ == "__main__":
    book_manager = Book()
    book_manager.display_books()
