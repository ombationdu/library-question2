#! /usr/bin/python3
import tkinter as tk
from tkinter import messagebox
from book import Book
from member import Member
from issue import Issue

class AdminInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System - Admin Interface")
        
        self.book_manager = Book()
        self.member_manager = Member()
        self.issue_manager = Issue()

        self.create_widgets()

    def create_widgets(self):
        self.add_book_frame = tk.LabelFrame(self.root, text="Add Book")
        self.add_book_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.add_book_frame, text="Title:").grid(row=0, column=0, sticky="e")
        self.title_entry = tk.Entry(self.add_book_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_book_frame, text="Author:").grid(row=1, column=0, sticky="e")
        self.author_entry = tk.Entry(self.add_book_frame)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_book_frame, text="Quantity:").grid(row=2, column=0, sticky="e")
        self.quantity_entry = tk.Entry(self.add_book_frame)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_book_btn = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_book_btn.grid(row=3, columnspan=2, pady=5)

        # Add Member Section
        self.add_member_frame = tk.LabelFrame(self.root, text="Add Member")
        self.add_member_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.add_member_frame, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.add_member_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_member_frame, text="Address:").grid(row=1, column=0, sticky="e")
        self.address_entry = tk.Entry(self.add_member_frame)
        self.address_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_member_frame, text="Type:").grid(row=2, column=0, sticky="e")
        self.type_entry = tk.Entry(self.add_member_frame)
        self.type_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_member_btn = tk.Button(self.add_member_frame, text="Add Member", command=self.add_member)
        self.add_member_btn.grid(row=3, columnspan=2, pady=5)

        # Issue Book Section
        self.issue_book_frame = tk.LabelFrame(self.root, text="Issue Book")
        self.issue_book_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.issue_book_frame, text="Book ID (Bno):").grid(row=0, column=0, sticky="e")
        self.book_id_entry = tk.Entry(self.issue_book_frame)
        self.book_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.issue_book_frame, text="Member ID:").grid(row=1, column=0, sticky="e")
        self.member_id_entry = tk.Entry(self.issue_book_frame)
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.issue_book_btn = tk.Button(self.issue_book_frame, text="Issue Book", command=self.issue_book)
        self.issue_book_btn.grid(row=2, columnspan=2, pady=5)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        quantity = int(self.quantity_entry.get())
        self.book_manager.add_book(title, author, quantity)
        messagebox.showinfo("Success", "Book added successfully.")

    def add_member(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        member_type = self.type_entry.get()
        self.member_manager.add_member(name, address, member_type)
        messagebox.showinfo("Success", "Member added successfully.")

    def issue_book(self):
        bno = int(self.book_id_entry.get())
        member_id = int(self.member_id_entry.get())
        self.issue_manager.issue_book(bno, member_id)
        messagebox.showinfo("Success", "Book issued successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    admin_interface = AdminInterface(root)
    root.mainloop()
