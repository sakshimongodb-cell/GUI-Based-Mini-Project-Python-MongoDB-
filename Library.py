import tkinter as tk
from tkinter import ttk, messagebox
import pymongo
import csv

# --- 1. DATABASE CONNECTION ---
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["SakshiMongoDB"]
    collection = db["Library"]
    client.server_info() 
except Exception as e:
    print(f"Connection Error: {e}")

# --- 2. THE LOGIN LOGIC ---
def check_login():
    # Credentials for your project
    if user_entry.get() == "admin" and pass_entry.get() == "123":
        login_window.destroy()  
        open_main_app()         
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# --- 3. THE MAIN APPLICATION WINDOW ---
def open_main_app():
    global root, title_entry, author_entry, isbn_entry, tree

    root = tk.Tk()
    root.title("Lumina Library Pro - Final Version")
    root.geometry("1000x550")

    # --- FUNCTIONS (The Search & Delete Updates) ---
    def refresh_table(search_query=None):
        for item in tree.get_children():
            tree.delete(item)
        
        # Search Filter Logic
        query = {}
        if search_query:
            query = {"isbn": {"$regex": search_query, "$options": "i"}}

        for book in collection.find(query):
            tree.insert("", "end", values=(book.get("title"), book.get("author"), book.get("isbn"), book.get("status")))

    def add_book():
        t = title_entry.get().strip() # Input Cleaning
        a = author_entry.get().strip()
        i = isbn_entry.get().strip()

        if not t or not i:
            messagebox.showwarning("Input Error", "Title and ISBN are required!")
            return

        try:
            collection.insert_one({"title": t, "author": a, "isbn": i, "status": "Available"})
            messagebox.showinfo("Success", f"'{t}' Added!")
            refresh_table()
        except Exception as e:
            messagebox.showerror("Error", "Validation failed in MongoDB")

    def delete_book():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Select a book to delete.")
            return
        
        isbn_val = tree.item(selected)['values'][2]
        if messagebox.askyesno("Confirm", "Delete this record?"):
            collection.delete_one({"isbn": str(isbn_val)})
            refresh_table()

    def export_csv():
        with open("Library_Report.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "author", "isbn", "status"], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(list(collection.find()))
        messagebox.showinfo("Export", "CSV Saved to your project folder!")

    # --- GUI LAYOUT ---
    # Sidebar
    sidebar = tk.LabelFrame(root, text=" Manage Inventory ", padx=20, pady=20)
    sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    tk.Label(sidebar, text="Book Title").pack(anchor="w")
    title_entry = tk.Entry(sidebar, width=30)
    title_entry.pack(pady=5)

    tk.Label(sidebar, text="Author").pack(anchor="w")
    author_entry = tk.Entry(sidebar, width=30)
    author_entry.pack(pady=5)

    tk.Label(sidebar, text="ISBN").pack(anchor="w")
    isbn_entry = tk.Entry(sidebar, width=30)
    isbn_entry.pack(pady=5)

    tk.Button(sidebar, text="Add Book", command=add_book, bg="green", fg="white", width=20).pack(pady=10)
    tk.Button(sidebar, text="Delete Selected", command=delete_book, bg="red", fg="white", width=20).pack(pady=5)
    tk.Button(sidebar, text="Export CSV", command=export_csv, bg="blue", fg="white", width=20).pack(pady=5)

    # Main Area (Search & Table)
    main_area = tk.Frame(root)
    main_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Search Bar Section
    search_frame = tk.Frame(main_area)
    search_frame.pack(fill=tk.X, pady=5)
    tk.Label(search_frame, text="Search ISBN:").pack(side=tk.LEFT)
    s_entry = tk.Entry(search_frame)
    s_entry.pack(side=tk.LEFT, padx=5)
    tk.Button(search_frame, text="Search", command=lambda: refresh_table(s_entry.get())).pack(side=tk.LEFT)
    tk.Button(search_frame, text="Reset", command=lambda: refresh_table()).pack(side=tk.LEFT, padx=5)

    # Table
    tree = ttk.Treeview(main_area, columns=("Title", "Author", "ISBN", "Status"), show="headings")
    for col in ("Title", "Author", "ISBN", "Status"): tree.heading(col, text=col)
    tree.pack(fill=tk.BOTH, expand=True)

    refresh_table()
    root.mainloop()

# --- START WITH LOGIN WINDOW ---
login_window = tk.Tk()
login_window.title("Lumina Login")
login_window.geometry("300x250")

tk.Label(login_window, text="Admin Login", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(login_window, text="Username").pack()
user_entry = tk.Entry(login_window)
user_entry.pack()
tk.Label(login_window, text="Password").pack()
pass_entry = tk.Entry(login_window, show="*")
pass_entry.pack()

tk.Button(login_window, text="Login", command=check_login, width=15).pack(pady=20)

login_window.mainloop()
