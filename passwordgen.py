import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    username = entry_name.get().strip()

    if username == "":
        messagebox.showwarning("Input Required", "Please enter your name.")
        return

    # Characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}<>?/"

    # Password length
    password_length = 14

    # First few characters come from username (if available)
    password = []

    for ch in username[:3]:
        if ch.isalpha():
            password.append(random.choice([ch.lower(), ch.upper()]))

    # Ensure password has at least one of each type
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(digits))
    password.append(random.choice(symbols))

    # Remaining random characters
    all_characters = lowercase + uppercase + digits + symbols

    while len(password) < password_length:
        password.append(random.choice(all_characters))

    # Shuffle for randomness
    random.shuffle(password)

    # Display password
    password_var.set("".join(password))


def copy_password():
    password = password_var.get()

    if password == "":
        messagebox.showinfo("Nothing to Copy", "Generate a password first.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("450x260")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Strong Password Generator",
    font=("Arial", 16, "bold")
)
title.pack(pady=15)

name_label = tk.Label(root, text="Enter Username:")
name_label.pack()

entry_name = tk.Entry(root, width=35, font=("Arial", 11))
entry_name.pack(pady=5)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
    width=20
)
generate_btn.pack(pady=10)

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=35,
    font=("Courier New", 12),
    justify="center"
)
password_entry.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#2196F3",
    fg="white",
    width=20
)
copy_btn.pack(pady=5)

root.mainloop()