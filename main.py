import secrets
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def calculate_strength(password):
    length = len(password)
    if length >= 12:
        return "Strong"
    elif length >= 8:
        return "Medium"
    else:
        return "Weak"

def generate_and_display_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError
        password = generate_password(password_length)
        strength = calculate_strength(password)
        password_display.config(text=password)
        strength_display.config(text=f"Strength: {strength}")
    except ValueError:
        password_display.config(text="Please enter a valid length.")
        strength_display.config(text="")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_display.cget("text"))

root = tk.Tk()
root.title("Password Generator")
root.geometry("230x230")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("-apple-system, BlinkMacSystemFont, sans-serif", 12))
style.configure("TButton", font=("-apple-system, BlinkMacSystemFont, sans-serif", 12), padding=6)
style.configure("TEntry", font=("-apple-system, BlinkMacSystemFont, sans-serif", 30))

main_frame = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

length_label = ttk.Label(main_frame, text="Enter Length:", style="TLabel")
length_label.grid(column=0, row=0, sticky=(tk.W, tk.E), pady=(0, 5))

length_entry = ttk.Entry(main_frame, style="TEntry")
length_entry.grid(column=0, row=1, sticky=(tk.W, tk.E), pady=(0, 10))

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_and_display_password, style="TButton")
generate_button.grid(column=0, row=2, pady=(0, 10))

password_display = ttk.Label(main_frame, text="", style="TLabel")
password_display.grid(column=0, row=3, pady=(0, 10))

strength_display = ttk.Label(main_frame, text="", style="TLabel")
strength_display.grid(column=0, row=4, pady=(0, 10))

copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard, style="TButton")
copy_button.grid(column=0, row=5)

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
