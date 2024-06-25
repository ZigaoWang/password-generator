import secrets
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def calculate_strength(password):
    length = len(password)
    if length < 8:
        return "Weak"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and (has_upper or has_lower) and has_digit and has_special:
        return "Medium"
    else:
        return "Weak"


def generate_and_display_password():
    try:
        password_length = int(length_entry.get())
        if password_length < 4 or password_length > 64:
            raise ValueError("Length must be between 4 and 64.")

        password = generate_password(password_length)
        strength = calculate_strength(password)
        password_display.config(text=password)
        strength_display.config(text=f"Strength: {strength}")
    except ValueError as ve:
        password_display.config(text=str(ve))
        strength_display.config(text="")


def copy_to_clipboard():
    password = password_display.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("-apple-system, BlinkMacSystemFont, sans-serif", 12))
style.configure("TButton", font=("-apple-system, BlinkMacSystemFont, sans-serif", 12), padding=6)
style.configure("TEntry", font=("-apple-system, BlinkMacSystemFont, sans-serif", 12))

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

length_label = ttk.Label(main_frame, text="Enter Length (4-64):")
length_label.grid(column=0, row=0, sticky=(tk.W, tk.E), pady=(0, 5))

length_entry = ttk.Entry(main_frame)
length_entry.grid(column=0, row=1, sticky=(tk.W, tk.E), pady=(0, 10))

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(column=0, row=2, pady=(0, 10))

password_display = ttk.Label(main_frame, text="", wraplength=250)
password_display.grid(column=0, row=3, pady=(0, 10))

strength_display = ttk.Label(main_frame, text="")
strength_display.grid(column=0, row=4, pady=(0, 10))

copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(column=0, row=5)

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()