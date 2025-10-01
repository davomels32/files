from tkinter import *
from tkinter import messagebox
import json, os

DATA_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE,'w') as f:
        json.dump(expenses,f,indent=4)

# === CLI ===
def expense_tracker_cli():
    print("\n=== Expense Tracker (CLI) ===")
    expenses = load_expenses()
    while True:
        print("\nCommands: add | view | edit | delete | summary | quit")
        cmd = input("> ").strip().lower()
        if cmd == "add":
            title = input("Title: ").strip()
            amount = float(input("Amount: "))
            category = input("Category: ").strip() or "General"
            expenses.append({"title": title, "amount": amount, "category": category})
            save_expenses(expenses); print("Added.")
        elif cmd == "view":
            if not expenses: print("No expenses yet.")
            else:
                total = 0.0
                for i,e in enumerate(expenses,1):
                    print(f"{i}. {e['title']} - {e['amount']:.2f'} ({e['category']})".replace("'", ''))
                    total += e['amount']
                print(f"Total: {total:.2f}")
        elif cmd == "edit":
            idx = int(input("Expense number to edit: ")) - 1
            if idx<0 or idx>=len(expenses): print("Invalid index"); continue
            e = expenses[idx]
            print("Leave blank to keep current value.")
            t = input(f"Title [{e['title']}]: ").strip() or e['title']
            a_in = input(f"Amount [{e['amount']}]: ").strip()
            a = float(a_in) if a_in else e['amount']
            c = input(f"Category [{e['category']}]: ").strip() or e['category']
            expenses[idx] = {'title':t,'amount':a,'category':c}
            save_expenses(expenses); print('Updated.')
        elif cmd == 'delete':
            idx = int(input('Expense number to delete: ')) -1
            if 0<=idx<len(expenses):
                expenses.pop(idx); save_expenses(expenses); print('Deleted.')
            else: print('Invalid index.')
        elif cmd == 'summary':
            if not expenses: print('No expenses.')
            else:
                summary={}
                for e in expenses:
                    summary.setdefault(e['category'],0); summary[e['category']]+=e['amount']
                for k,v in summary.items(): print(f"{k}: {v:.2f}")
        elif cmd == 'quit': break
        else: print('Unknown command.')

# === GUI ===
def expense_tracker_gui():
    expenses = load_expenses()
    window = Tk(); window.title('Expense Tracker')
    Label(window, text='Title:').grid(row=0,column=0,sticky='e')
    e_title = Entry(window); e_title.grid(row=0,column=1)
    Label(window, text='Amount:').grid(row=1,column=0,sticky='e')
    e_amount = Entry(window); e_amount.grid(row=1,column=1)
    Label(window, text='Category:').grid(row=2,column=0,sticky='e')
    e_cat = Entry(window); e_cat.grid(row=2,column=1)
    lb = Listbox(window, width=60); lb.grid(row=4,column=0,columnspan=3,pady=8)
    def refresh():
        lb.delete(0,END)
        for i,e in enumerate(expenses,1):
            lb.insert(END, f"{i}. {e['title']} - {e['amount']:.2f} ({e['category']})")
    def add_expense():
        try:
            t = e_title.get().strip(); a = float(e_amount.get().strip()); c = e_cat.get().strip() or 'General'
        except:
            messagebox.showerror('Error','Enter a valid amount'); return
        expenses.append({'title':t,'amount':a,'category':c}); save_expenses(expenses); refresh()
        e_title.delete(0,END); e_amount.delete(0,END); e_cat.delete(0,END)
    def edit_selected():
        sel = lb.curselection()
        if not sel: messagebox.showinfo('Info','Select an item'); return
        idx = sel[0]
        e = expenses[idx]
        # simple popup to edit
        top = Toplevel(window); top.title('Edit Expense')
        Label(top, text='Title:').grid(row=0,column=0); te = Entry(top); te.grid(row=0,column=1); te.insert(0,e['title'])
        Label(top, text='Amount:').grid(row=1,column=0); ae = Entry(top); ae.grid(row=1,column=1); ae.insert(0,str(e['amount']))
        Label(top, text='Category:').grid(row=2,column=0); ce = Entry(top); ce.grid(row=2,column=1); ce.insert(0,e['category'])
        def save_edit():
            try:
                e['title'] = te.get().strip(); e['amount'] = float(ae.get().strip()); e['category'] = ce.get().strip() or 'General'
                save_expenses(expenses); refresh(); top.destroy(); messagebox.showinfo('Saved','Expense updated')
            except:
                messagebox.showerror('Error','Invalid amount')
        Button(top, text='Save', command=save_edit).grid(row=3,column=0,columnspan=2,pady=6)
    def delete_selected():
        sel = lb.curselection()
        if not sel: messagebox.showinfo('Info','Select an item'); return
        idx = sel[0]; expenses.pop(idx); save_expenses(expenses); refresh(); messagebox.showinfo('Deleted','Expense removed')
    def show_summary():
        if not expenses: messagebox.showinfo('Summary','No expenses'); return
        summary={}
        for e in expenses:
            summary.setdefault(e['category'],0); summary[e['category']]+=e['amount']
        messagebox.showinfo('Summary', '\n'.join([f"{k}: {v:.2f}" for k,v in summary.items()]))
    Button(window, text='Add', command=add_expense).grid(row=3,column=0,pady=6)
    Button(window, text='Edit Selected', command=edit_selected).grid(row=3,column=1,pady=6)
    Button(window, text='Delete Selected', command=delete_selected).grid(row=3,column=2,pady=6)
    Button(window, text='Summary', command=show_summary).grid(row=5,column=0,pady=6)
    refresh(); window.mainloop()

if __name__ == '__main__':
    print('Choose: 1) CLI 2) GUI'); ch = input('> ').strip()
    if ch == '1': expense_tracker_cli()
    else: expense_tracker_gui()
