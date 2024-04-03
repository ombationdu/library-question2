from book import Book
from issue import Issue
from member import Member

class LibraryManagement:
    def __init__(self):
        self.book_manager = Book()
        self.issue_manager = Issue()
        self.member_manager = Member()

    def display_statistics(self):
        try:
            # Count total books
            self.book_manager.cursor.execute("SELECT COUNT(*) FROM bookRecord")
            total_books = self.book_manager.cursor.fetchone()[0]

            # Count total members
            self.member_manager.cursor.execute("SELECT COUNT(*) FROM member")
            total_members = self.member_manager.cursor.fetchone()[0]

            # Count total issued books
            self.issue_manager.cursor.execute("SELECT COUNT(*) FROM issue")
            total_issued_books = self.issue_manager.cursor.fetchone()[0]

            print("======= Library Statistics =======")
            print(f"Total Books: {total_books}")
            print(f"Total Members: {total_members}")
            print(f"Total Issued Books: {total_issued_books}")
            print("==================================")
        except Exception as e:
            print("Error displaying statistics:", e)

    def manage_overdue_books(self):
        try:
            # Retrieve overdue books
            self.issue_manager.cursor.execute("SELECT * FROM issue WHERE DueDate < CURDATE()")
            overdue_books = self.issue_manager.cursor.fetchall()

            if overdue_books:
                print("======= Overdue Books =======")
                print("IssueID\tBno\tMemberID\tIssueDate\tDueDate")
                for issue in overdue_books:
                    print(f"{issue[0]}\t{issue[1]}\t{issue[2]}\t{issue[3]}\t{issue[4]}")
                print("=============================")
            else:
                print("No overdue books.")
        except Exception as e:
            print("Error managing overdue books:", e)

    def run(self):
        while True:
            print("======= LIBRARY MANAGEMENT =======")
            print("1. Display Statistics")
            print("2. Manage Overdue Books")
            print("3. Exit")
            print("===================================")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_statistics()
            elif choice == "2":
                self.manage_overdue_books()
            elif choice == "3":
                print("Exiting Library Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    library_management = LibraryManagement()
    library_management.run()
