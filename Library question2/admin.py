from book import Book
from issue import Issue
from member import Member

class LibraryManagement:
    def __init__(self):
        self.book_manager = Book()
        self.issue_manager = Issue()
        self.member_manager = Member()

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        quantity = int(input("Enter book quantity: "))
        self.book_manager.add_book(title, author, quantity)

    def add_member(self):
        name = input("Enter member name: ")
        address = input("Enter member address: ")
        member_type = input("Enter member type: ")
        self.member_manager.add_member(name, address, member_type)

    def issue_book(self):
        bno = int(input("Enter book number (Bno): "))
        member_id = int(input("Enter member ID: "))
        self.issue_manager.issue_book(bno, member_id)

    def run_admin_interface(self):
        while True:
            print("======= ADMIN INTERFACE =======")
            print("1. Add Book")
            print("2. Add Member")
            print("3. Issue Book")
            print("4. Exit")
            print("===============================")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.add_member()
            elif choice == "3":
                self.issue_book()
            elif choice == "4":
                print("Exiting Admin Interface.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    admin_interface = LibraryManagement()
    admin_interface.run_admin_interface()
