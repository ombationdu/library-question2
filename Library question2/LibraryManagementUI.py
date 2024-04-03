#! /usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from book import Book
from issue import Issue
from member import Member

class LibraryManagementUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x300")

        self.book_manager = Book()
        self.issue_manager = Issue()
        self.member_manager = Member()

        self.create_widgets()

    def create_widgets(self):
        # Create buttons
        btn_statistics = tk.Button(self.root, text="Display Statistics", command=self.display_statistics)
        btn_statistics.pack(pady=10)

        btn_overdue_books = tk.Button(self.root, text="Manage Overdue Books", command=self.manage_overdue_books)
        btn_overdue_books.pack(pady=10)

        btn_exit = tk.Button(self.root, text="Exit", command=self.root.quit)
        btn_exit.pack(pady=10)

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

            messagebox.showinfo("Library Statistics", 
                f"Total Books: {total_books}\nTotal Members: {total_members}\nTotal Issued Books: {total_issued_books}")

        except Exception as e:
            messagebox.showerror("Error", f"Error displaying statistics: {e}")

    def manage_overdue_books(self):
        try:
            # Retrieve overdue books
            self.issue_manager.cursor.execute("SELECT * FROM issue WHERE DueDate < CURDATE()")
            overdue_books = self.issue_manager.cursor.fetchall()

            if overdue_books:
                message = "======= Overdue Books =======\n"
                for issue in overdue_books:
                    message += f"IssueID: {issue[0]}, Bno: {issue[1]}, MemberID: {issue[2]}, IssueDate: {issue[3]}, DueDate: {issue[4]}\n"
                messagebox.showinfo("Overdue Books", message)
            else:
                messagebox.showinfo("Overdue Books", "No overdue books.")

        except Exception as e:
            messagebox.showerror("Error", f"Error managing overdue books: {e}")

def main():
    root = tk.Tk()
    app = LibraryManagementUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
