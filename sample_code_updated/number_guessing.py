from tkinter import *
from tkinter import messagebox
import random, json, os

SETTINGS_FILE = 'guess_settings.json'

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE,'r') as f:
            return json.load(f)
    return {'low':1,'high':100}

def save_settings(s):
    with open(SETTINGS_FILE,'w') as f:
        json.dump(s,f,indent=4)

def guessing_cli():
    s = load_settings(); low = s['low']; high = s['high']
    print(f"\n=== Number Guessing (CLI) - range {low}-{high} ===")
    target = random.randint(low,high); tries=0
    while True:
        guess = int(input('Your guess: ')); tries+=1
        if guess==target: print(f"Correct! {tries} tries."); break
        elif guess<target: print('Too low') 
        else: print('Too high')

def guessing_gui():
    s = load_settings(); low=s['low']; high=s['high']
    target = {'val': random.randint(low,high)}; tries={'val':0}
    window = Tk(); window.title('Number Guessing')
    Label(window, text=f'Guess a number {low}-{high}').grid(row=0,column=0)
    e = Entry(window); e.grid(row=1,column=0)
    res = Label(window, text=''); res.grid(row=2,column=0)
    def make_guess():
        try: g=int(e.get().strip())
        except: res.config(text='Enter a number'); return
        tries['val']+=1
        if g==target['val']: res.config(text=f'Correct! {tries["val"]} tries')
        elif g<target['val']: res.config(text='Too low')
        else: res.config(text='Too high')
    def reset(): target['val']=random.randint(low,high); tries['val']=0; res.config(text=''); e.delete(0,END)
    Button(window, text='Guess', command=make_guess).grid(row=3,column=0,pady=4)
    Button(window, text='Reset', command=reset).grid(row=3,column=1,pady=4)
    Button(window, text='Settings', command=lambda: open_settings(window)).grid(row=4,column=0,pady=4)
    window.mainloop()

def open_settings(parent):
    s = load_settings()
    top = Toplevel(parent); top.title('Settings')
    Label(top, text='Low:').grid(row=0,column=0); le=Entry(top); le.grid(row=0,column=1); le.insert(0,str(s['low']))
    Label(top, text='High:').grid(row=1,column=0); he=Entry(top); he.grid(row=1,column=1); he.insert(0,str(s['high']))
    def save():
        try:
            nl = int(le.get().strip()); nh = int(he.get().strip())
            if nl>=nh: messagebox.showerror('Error','Low must be < High'); return
            save_settings({'low':nl,'high':nh}); messagebox.showinfo('Saved','Settings updated'); top.destroy()
        except:
            messagebox.showerror('Error','Enter valid integers')
    Button(top, text='Save', command=save).grid(row=2,column=0,columnspan=2,pady=6)

if __name__ == '__main__':
    print('Choose: 1) CLI 2) GUI'); ch=input('> ').strip()
    if ch=='1': guessing_cli()
    else: guessing_gui()
