import random
import tkinter as tk


def check_guess(event=None):
    global attempts, secret_number

    guess = entry.get().strip()

    if not guess.isdigit():
        result_label.config(
            text="⚠ Please enter a valid positive integer!", fg="#FF6B6B"
        )
        entry.delete(0, tk.END)
        return

    guess = int(guess)
    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    if guess < secret_number:
        result_label.config(
            text="📉 Too low! Try a higher number.", fg="#FFD700"
        )
    elif guess > secret_number:
        result_label.config(
            text="📈 Too high! Try a lower number.", fg="#FFD700"
        )
    else:
        result_label.config(
            text=f"🎉 Correct! You guessed it in {attempts} attempts!",
            fg="#4CAF50",
        )
        entry.config(state="disabled")
        guess_button.config(state="disabled")

    entry.delete(0, tk.END)


def restart_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    attempts_label.config(text="Attempts: 0")
    result_label.config(text="Guess a number from 1 to 100", fg="#FFD700")

    entry.config(state="normal")
    guess_button.config(state="normal")
    entry.delete(0, tk.END)
    entry.focus_set()


# Main Window Configuration
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("500x450")
window.config(bg="#1e1e2f")

# Global Game Variables
secret_number = random.randint(1, 100)
attempts = 0

# UI Components
title_label = tk.Label(
    window,
    text="🎯 Number Guessing Game",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white",
)
title_label.pack(pady=(25, 5))

instruction_label = tk.Label(
    window,
    text="I picked a number between 1 and 100",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="lightgray",
)
instruction_label.pack(pady=5)

attempts_label = tk.Label(
    window,
    text="Attempts: 0",
    font=("Arial", 11, "italic"),
    bg="#1e1e2f",
    fg="#A0A0B0",
)
attempts_label.pack(pady=5)

entry = tk.Entry(
    window,
    font=("Arial", 18),
    width=10,
    justify="center",
    bd=2,
    relief="solid",
)
entry.pack(pady=10)
entry.focus_set()

# Bind the Enter key to check_guess
window.bind("<Return>", check_guess)

guess_button = tk.Button(
    window,
    text="Check Guess",
    font=("Arial", 13, "bold"),
    command=check_guess,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    width=15,
    cursor="hand2",
)
guess_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="Guess a number from 1 to 100",
    font=("Arial", 13),
    bg="#1e1e2f",
    fg="#FFD700",
    wraplength=450,
)
result_label.pack(pady=15)

restart_button = tk.Button(
    window,
    text="🔄 Restart Game",
    font=("Arial", 11),
    command=restart_game,
    bg="#2196F3",
    fg="white",
    activebackground="#0b7dda",
    activeforeground="white",
    cursor="hand2",
)
restart_button.pack(pady=10)

window.mainloop()