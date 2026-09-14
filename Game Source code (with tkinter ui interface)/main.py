import tkinter as tk
import random

# Generate random number from 1 to 100
secret_number = random.randint(1, 100)

attempts = 0


def check_guess():
    global attempts
    global secret_number

    guess = entry.get()

    # Check if input is a number
    if not guess.isdigit():
        result_label.config(text="⚠ Enter a valid number!")
        return

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        result_label.config(
            text="📉 Too low! Try a higher number."
        )

    elif guess > secret_number:
        result_label.config(
            text="📈 Too high! Try a lower number."
        )

    else:
        result_label.config(
            text=f"🎉 Correct! You guessed it in {attempts} attempts!"
        )


def restart_game():
    global secret_number
    global attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    entry.delete(0, tk.END)
    result_label.config(text="Guess a number from 1 to 100")


# Create main window
window = tk.Tk()

window.title("Number Guessing Game")
window.geometry("500x400")

# Background color
window.config(bg="#1e1e2f")


# Title
title_label = tk.Label(
    window,
    text="🎯 Number Guessing Game",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title_label.pack(pady=30)


# Instructions
instruction_label = tk.Label(
    window,
    text="I picked a number between 1 and 100",
    font=("Arial", 13),
    bg="#1e1e2f",
    fg="lightgray"
)

instruction_label.pack(pady=10)


# Input box
entry = tk.Entry(
    window,
    font=("Arial", 18),
    width=10,
    justify="center"
)

entry.pack(pady=15)


# Guess button
guess_button = tk.Button(
    window,
    text="Check Guess",
    font=("Arial", 14),
    command=check_guess,
    bg="#4CAF50",
    fg="white",
    width=15
)

guess_button.pack(pady=10)


# Result / hint label
result_label = tk.Label(
    window,
    text="Guess a number from 1 to 100",
    font=("Arial", 13),
    bg="#1e1e2f",
    fg="#FFD700"
)

result_label.pack(pady=20)


# Restart button
restart_button = tk.Button(
    window,
    text="🔄 Restart Game",
    font=("Arial", 12),
    command=restart_game,
    bg="#2196F3",
    fg="white"
)

restart_button.pack(pady=10)


# Start GUI
window.mainloop()