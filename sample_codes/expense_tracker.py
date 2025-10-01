from tkinter import *
from tkinter import messagebox
import json, os

# === Expense Tracker (CLI + GUI) in user's style ===
DATA_FILE = "expenses.json"

# === Load / Save ===
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# === CLI ===
def expense_tracker_cli():
    print("\n=== Expense Tracker (CLI) ===")
    expenses = load_expenses()
    while True:
        print("\nCommands: add | view | summary | quit")
        cmd = input("> ").strip().lower()
        if cmd == "add":
            title = input("Title: ").strip()
            amount = float(input("Amount: "))
            category = input("Category: ").strip() or "General"
            expenses.append({"title": title, "amount": amount, "category": category})
            save_expenses(expenses)
            print("Added.")
        elif cmd == "view":
            if not expenses:
                print("No expenses yet.")
            else:
                total = 0.0
                for i, e in enumerate(expenses,1):
                    print(f"{i}. {e['title']} - {e['amount']:.2f} ({e['category']})")
                    total += e['amount']
                print(f"Total: {total:.2f}")
        elif cmd == "summary":
            if not expenses:
                print("No expenses.")
            else:
                summary = {}
                for e in expenses:
                    summary.setdefault(e['category'],0)
                    summary[e['category']] += e['amount']
                for k,v in summary.items():
                    print(f"{k}: {v:.2f}")
        elif cmd == "quit":
            break
        else:
            print("Unknown command.")

# === GUI ===
def expense_tracker_gui():
    expenses = load_expenses()  # list of dicts
    window = Tk()
    window.title("Expense Tracker")
    # --- Entries ---
    Label(window, text="Title:").grid(row=0,column=0,sticky="e")
    e_title = Entry(window); e_title.grid(row=0,column=1)
    Label(window, text="Amount:").grid(row=1,column=0,sticky="e")
    e_amount = Entry(window); e_amount.grid(row=1,column=1)
    Label(window, text="Category:").grid(row=2,column=0,sticky="e")
    e_cat = Entry(window); e_cat.grid(row=2,column=1)
    # --- Listbox ---
    lb = Listbox(window, width=50); lb.grid(row=4,column=0,columnspan=2,pady=8)
    def refresh_list():
        lb.delete(0,END)
        for e in expenses:
            lb.insert(END, f"{e['title']} - {e['amount']:.2f} ({e['category']})")
    def add_expense():
        try:
            t = e_title.get().strip()
            a = float(e_amount.get().strip())
            c = e_cat.get().strip() or "General"
        except ValueError:
            messagebox.showerror("Error","Enter a valid amount")
            return
        expenses.append({"title":t,"amount":a,"category":c})
        save_expenses(expenses)
        refresh_list()
        e_title.delete(0,END); e_amount.delete(0,END); e_cat.delete(0,END)
    def show_summary():
        if not expenses:
            messagebox.showinfo("Summary","No expenses")
            return
        summary = {}
        for e in expenses:
            summary.setdefault(e['category'],0)
            summary[e['category']] += e['amount']
        text = "\n".join([f"{k}: {v:.2f}" for k,v in summary.items()])
        messagebox.showinfo("Summary By Category", text)
    Button(window, text="Add", command=add_expense).grid(row=3,column=0,pady=6)
    Button(window, text="Summary", command=show_summary).grid(row=3,column=1,pady=6)
    refresh_list()
    window.mainloop()

# --- Run helpers if module executed directly ---
if __name__ == "__main__":
    print("Choose: 1) CLI  2) GUI")
    ch = input("> ").strip()
    if ch == "1":
        expense_tracker_cli()
    else:
        expense_tracker_gui()
