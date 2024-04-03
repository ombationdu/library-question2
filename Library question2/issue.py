import mysql.connector
from datetime import datetime, timedelta

class Issue:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="Library"
        )
        self.cursor = self.db_connection.cursor()

    def get_issued_books_count(self, member_id):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM issue WHERE MemberID=%s", (member_id,))
            count = self.cursor.fetchone()[0]
            return count
        except mysql.connector.Error as error:
            print("Error getting issued books count:", error)
            return -1

    def issue_book(self, bno, member_id):
        try:
            # Check if member already has 3 books issued
            issued_books_count = self.get_issued_books_count(member_id)
            if issued_books_count >= 3:
                print("Cannot issue more than 3 books to a member.")
                return

            # Check if the book is available
            self.cursor.execute("SELECT Available FROM bookRecord WHERE Bno=%s", (bno,))
            available = self.cursor.fetchone()[0]
            if available > 0:
                # Reduce available quantity of the book
                self.cursor.execute("UPDATE bookRecord SET Available = Available - 1 WHERE Bno=%s", (bno,))
                self.db_connection.commit()

                # Get current date and due date (10 days from now)
                issue_date = datetime.now().date()
                due_date = issue_date + timedelta(days=10)

                # Issue the book
                sql = "INSERT INTO issue (Bno, MemberID, IssueDate, DueDate) VALUES (%s, %s, %s, %s)"
                issue_data = (bno, member_id, issue_date, due_date)
                self.cursor.execute(sql, issue_data)
                self.db_connection.commit()

                print("Book issued successfully.")
            else:
                print("Book not available for issue.")
        except mysql.connector.Error as error:
            print("Error issuing book:", error)

    # Other methods remain the same...

if __name__ == "__main__":
    issue_manager = Issue()
    issue_manager.issue_book(1, 1)  # Example: Issue book with Bno 1 to Member with MemberID 1
