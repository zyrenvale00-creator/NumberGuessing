import tkinter as t
import random

lowNum = 1
highNum = 10
number = random.randint(lowNum, highNum)
attempts = 0

def guess():
    global attempts
    try:
        user_guess = int(guess_entry.get())

        if user_guess < lowNum or user_guess > highNum:
            result.config(
                text=f"Enter a number between {lowNum} and {highNum}",
                fg="red"
            )
            guess_entry.delete(0, t.END)
            return
            
        attempts += 1
        attempts_label.config(text=f"ATTEMPTS | {attempts}")

        if user_guess < number:
            result.config(text="Too low!!", fg="#5FE2F7")
        elif user_guess > number:
            result.config(text="Too high!!", fg="#5FE2F7")
        else:
            result.config(text=f"Correct!! The number was {number}", fg="#5FF799")
            guess_button.config(state="disabled")

        guess_entry.delete(0, t.END)

    except ValueError:
        result.config(text="Please enter a valid number!", fg="red")
        guess_entry.delete(0, t.END)

# Main Window
my = t.Tk()
my.title("Number Guessing Game")
my.geometry("600x500")
my.resizable(False, False)
my.configure(bg="#111827")

main_frame = t.Frame(
    my,
    bg="#172033",
    padx=45,
    pady=35
)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = t.Label(
    main_frame,
    text="Number Guessing Game",
    font=("Nectar", 25, "bold"),
    fg="#A78BFA",
    bg="#172033",
    cursor="xterm"
)
title.pack(pady=25)

# Instructions
instruction = t.Label(
    main_frame,
    text="Guessing a number between 1-10",
    font=("Arial", 18),
    fg="#9CA3AF",
    bg="#172033",
    cursor="xterm"
)
instruction.pack()

# Input
guess_entry = t.Entry(
    main_frame,
    font=("Arial", 16),
    fg="#F9FAFB",
    width=15,
    bg="#263249",
    insertbackground="#A78BFA",
    justify="center", 
    relief="flat",
    bd = 0,
    cursor="xterm"
)
guess_entry.pack(ipady=8, pady=(15, 18))

# Result
result_frame = t.Frame(
    main_frame,
    bg="#263249",
    padx=7,
    pady=7
)
result_frame.pack(fill="x", pady=(0, 7))

result = t.Label(
    result_frame,
    text="Enter a guess to start...",
    font=("Arial", 12),
    fg="#F9FAFB",
    bg="#263249",
    cursor="xterm"
)
result.pack(pady=10)

# Guess Button
guess_button = t.Button(
    main_frame,
    text="GUESS",
    font=("Arial", 12, "bold"),
    fg="#000000",
    bg="#A78BFA",
    activebackground="#C4B5FD",
    activeforeground="#111827",
    command=guess,
    width=18,
    height=2,
    cursor="hand2"
)
guess_button.pack(pady=10)

# Attempts
attempts_label = t.Label(
    main_frame,
    text="ATTEMPTS | 0",
    font=("Arial", 12, "bold"),
    fg="#5A8FEA",
    bg="#172033",
    cursor="xterm"
)
attempts_label.pack(pady=5)

#Enter 
guess_entry.bind("<Return>", lambda event: guess())

#autoPointToText
guess_entry.focus_set()

#Run app
my.mainloop()