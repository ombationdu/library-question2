import tkinter as tk
from tkinter import messagebox
from book import Book
from issue import Issue
from member import Member

class LibraryManagementUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.library_management = LibraryManagement()

        self.label = tk.Label(self.frame, text="Welcome to Library Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.button_statistics = tk.Button(self.frame, text="Display Statistics", command=self.display_statistics)
        self.button_statistics.pack(pady=5)

        self.button_overdue = tk.Button(self.frame, text="Manage Overdue Books", command=self.manage_overdue_books)
        self.button_overdue.pack(pady=5)

        self.button_exit = tk.Button(self.frame, text="Exit", command=self.exit_program)
        self.button_exit.pack(pady=5)

    def display_statistics(self):
        try:
            self.library_management.display_statistics()
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying statistics: {e}")

    def manage_overdue_books(self):
        try:
            self.library_management.manage_overdue_books()
        except Exception as e:
            messagebox.showerror("Error", f"Error managing overdue books: {e}")

    def exit_program(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.master.destroy()

class LibraryManagement:
    def __init__(self):
        self.book_manager = Book()
        self.issue_manager = Issue()
        self.member_manager = Member()

    def display_statistics(self):
        # Your existing display_statistics method code

    def manage_overdue_books(self):
        # Your existing manage_overdue_books method code

def main():
    root = tk.Tk()
    app = LibraryManagementUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
