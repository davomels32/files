from tkinter import *
from tkinter import messagebox
import random

def guessing_cli():
    print("\n=== Number Guessing (CLI) ===")
    low, high = 1, 100
    target = random.randint(low,high)
    tries = 0
    print(f"I chose a number between {low} and {high}")
    while True:
        guess = int(input("Your guess: "))
        tries += 1
        if guess == target:
            print(f"Correct! {tries} tries."); break
        elif guess < target:
            print("Too low")
        else:
            print("Too high")

def guessing_gui():
    target = {"val": random.randint(1,100)}
    tries = {"val":0}
    window = Tk(); window.title("Number Guessing")
    Label(window, text="Guess a number 1-100").grid(row=0,column=0)
    e = Entry(window); e.grid(row=1,column=0)
    res = Label(window, text=""); res.grid(row=2,column=0)
    def make_guess():
        try:
            g = int(e.get().strip())
        except:
            res.config(text="Enter a number"); return
        tries['val'] += 1
        if g == target['val']:
            res.config(text=f"Correct! {tries['val']} tries")
        elif g < target['val']:
            res.config(text="Too low")
        else:
            res.config(text="Too high")
    def reset():
        target['val'] = random.randint(1,100); tries['val']=0; res.config(text=""); e.delete(0,END)
    Button(window, text="Guess", command=make_guess).grid(row=3,column=0,pady=4)
    Button(window, text="Reset", command=reset).grid(row=3,column=1,pady=4)
    window.mainloop()

if __name__ == '__main__':
    print("Choose 1) CLI 2) GUI")
    ch = input("> ").strip()
    if ch == '1': guessing_cli()
    else: guessing_gui()
