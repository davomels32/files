from tkinter import *
from tkinter import messagebox
import json, os

DATA_FILE = 'students.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r') as f:
            return json.load(f)
    return {}

def save_data(students):
    with open(DATA_FILE,'w') as f:
        json.dump(students,f,indent=4)

students = load_data()

def sign_up():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    confirm = entry_confirm.get().strip()
    if username in students:
        messagebox.showerror('Error','Username exists'); return
    if password != confirm:
        messagebox.showerror('Error','Passwords do not match'); return
    profile = {
        'Full Name': entry_fullname.get().strip(),
        'Gender': entry_gender.get().strip(),
        'Date of Birth': entry_dob.get().strip(),
        'Email': entry_email.get().strip(),
        'Phone': entry_phone.get().strip(),
        'Program': entry_program.get().strip(),
        'Level': entry_level.get().strip()
    }
    students[username] = {'password':password,'profile':profile}
    save_data(students)
    messagebox.showinfo('Success', f'Account created for {username}')
    clear_entries()

def login():
    username = entry_login_user.get().strip(); password = entry_login_pass.get().strip()
    if username in students and students[username]['password'] == password:
        messagebox.showinfo('Welcome', f'Welcome {username}'); view_profile(username)
    else:
        messagebox.showerror('Error','Invalid credentials')

def view_profile(username):
    profile = students[username]['profile']
    w = Toplevel(window); w.title(f"{username} - Profile")
    r = 0
    for k,v in profile.items():
        Label(w, text=f"{k}: {v}").grid(row=r,column=0,sticky='w',padx=8,pady=2); r+=1

def clear_entries():
    for e in [entry_username,entry_password,entry_confirm,entry_fullname,entry_gender,entry_dob,entry_email,entry_phone,entry_program,entry_level]:
        e.delete(0,END)

window = Tk(); window.title('Student Registration')
Label(window, text='--- Register ---', font=('Arial',14,'bold')).grid(row=0,column=0,columnspan=2,pady=8)
Label(window, text='Username:').grid(row=1,column=0,sticky='e'); entry_username = Entry(window); entry_username.grid(row=1,column=1)
Label(window, text='Password:').grid(row=2,column=0,sticky='e'); entry_password = Entry(window, show='*'); entry_password.grid(row=2,column=1)
Label(window, text='Confirm Password:').grid(row=3,column=0,sticky='e'); entry_confirm = Entry(window, show='*'); entry_confirm.grid(row=3,column=1)
Label(window, text='Full Name:').grid(row=4,column=0,sticky='e'); entry_fullname = Entry(window); entry_fullname.grid(row=4,column=1)
Label(window, text='Gender:').grid(row=5,column=0,sticky='e'); entry_gender = Entry(window); entry_gender.grid(row=5,column=1)
Label(window, text='Date of Birth:').grid(row=6,column=0,sticky='e'); entry_dob = Entry(window); entry_dob.grid(row=6,column=1)
Label(window, text='Email:').grid(row=7,column=0,sticky='e'); entry_email = Entry(window); entry_email.grid(row=7,column=1)
Label(window, text='Phone:').grid(row=8,column=0,sticky='e'); entry_phone = Entry(window); entry_phone.grid(row=8,column=1)
Label(window, text='Program:').grid(row=9,column=0,sticky='e'); entry_program = Entry(window); entry_program.grid(row=9,column=1)
Label(window, text='Level:').grid(row=10,column=0,sticky='e'); entry_level = Entry(window); entry_level.grid(row=10,column=1)
Button(window, text='Register', bg='#7c6a6a', fg='white', command=sign_up).grid(row=11,column=0,columnspan=2,pady=6)

Label(window, text='--- Login ---', font=('Arial',14,'bold')).grid(row=12,column=0,columnspan=2,pady=8)
Label(window, text='Username:').grid(row=13,column=0,sticky='e'); entry_login_user = Entry(window); entry_login_user.grid(row=13,column=1)
Label(window, text='Password:').grid(row=14,column=0,sticky='e'); entry_login_pass = Entry(window, show='*'); entry_login_pass.grid(row=14,column=1)
Button(window, text='Login', bg='blue', fg='white', command=login).grid(row=15,column=0,columnspan=2,pady=6)

if __name__ == '__main__':
    window.mainloop()
