from tkinter import *
from tkinter import messagebox
import json, os

DATA_FILE = "library_books.json"

def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
    return {}

def save_books(books):
    with open(DATA_FILE,"w") as f:
        json.dump(books,f,indent=4)

# === CLI ===
def library_cli():
    print("\n=== Library System (CLI) ===")
    books = load_books()  # id -> info dict
    next_id = max([int(k) for k in books.keys()], default=0) + 1 if books else 1
    while True:
        print("\nCommands: add | list | borrow | return | quit")
        cmd = input("> ").strip().lower()
        if cmd == "add":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            books[str(next_id)] = {"title":title,"author":author,"available":True}
            next_id += 1
            save_books(books)
            print("Added.")
        elif cmd == "list":
            if not books:
                print("No books.")
            else:
                for bid,info in books.items():
                    status = "Available" if info["available"] else "Borrowed"
                    print(f"{bid}: {info['title']} by {info['author']} - {status}")
        elif cmd == "borrow":
            bid = input("Book id: ").strip()
            if bid not in books:
                print("No such book.")
            elif not books[bid]["available"]:
                print("Already borrowed.")
            else:
                books[bid]["available"] = False
                save_books(books)
                print("Borrowed.")
        elif cmd == "return":
            bid = input("Book id: ").strip()
            if bid in books:
                books[bid]["available"] = True
                save_books(books)
                print("Returned.")
            else:
                print("No such book.")
        elif cmd == "quit":
            break
        else:
            print("Unknown command.")

# === GUI ===
def library_gui():
    books = load_books()
    window = Tk(); window.title("Library System")
    # --- Entries ---
    Label(window, text="Title:").grid(row=0,column=0,sticky="e")
    e_title = Entry(window); e_title.grid(row=0,column=1)
    Label(window, text="Author:").grid(row=1,column=0,sticky="e")
    e_author = Entry(window); e_author.grid(row=1,column=1)
    lb = Listbox(window, width=60); lb.grid(row=3,column=0,columnspan=2,pady=8)
    def refresh():
        lb.delete(0,END)
        for bid,info in books.items():
            status = "Available" if info["available"] else "Borrowed"
            lb.insert(END, f"{bid}: {info['title']} by {info['author']} - {status}")
    def add_book():
        t = e_title.get().strip(); a = e_author.get().strip()
        if not t or not a:
            messagebox.showerror("Error","Title and Author required")
            return
        next_id = str(max([int(k) for k in books.keys()], default=0)+1) if books else "1"
        books[next_id] = {"title":t,"author":a,"available":True}
        save_books(books); refresh()
        e_title.delete(0,END); e_author.delete(0,END)
    def borrow_selected():
        sel = lb.curselection()
        if not sel:
            messagebox.showinfo("Info","Select an item first")
            return
        item = lb.get(sel[0])
        bid = item.split(":")[0]
        if not books[bid]["available"]:
            messagebox.showinfo("Info","Already borrowed")
            return
        books[bid]["available"] = False; save_books(books); refresh()
    def return_selected():
        sel = lb.curselection()
        if not sel:
            messagebox.showinfo("Info","Select an item first")
            return
        item = lb.get(sel[0]); bid = item.split(":")[0]
        books[bid]["available"] = True; save_books(books); refresh()
    Button(window, text="Add Book", command=add_book).grid(row=2,column=0,pady=6)
    Button(window, text="Borrow", command=borrow_selected).grid(row=2,column=1,pady=6)
    Button(window, text="Return", command=return_selected).grid(row=2,column=2,pady=6)
    refresh()
    window.mainloop()

if __name__ == "__main__":
    print("Choose: 1) CLI 2) GUI")
    ch = input("> ").strip()
    if ch == "1":
        library_cli()
    else:
        library_gui()
