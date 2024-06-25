import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError
        password = generate_password(password_length)
        password_display.config(text=password)
    except ValueError:
        password_display.config(text="Please enter a valid length.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_display.cget("text"))

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TEntry", font=("Helvetica", 14))

root.configure(bg='#2E3B4E')
main_frame = ttk.Frame(root, padding="20 20 20 20", style="TFrame")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(main_frame, text="Password Length:", background='#2E3B4E', foreground='#ffffff')
length_label.grid(column=0, row=0, sticky=(tk.W, tk.E))

length_entry = ttk.Entry(main_frame, justify='center')
length_entry.grid(column=0, row=1, sticky=(tk.W, tk.E), pady=(5, 15))

generate_button = ttk.Button(main_frame, text="Generate", command=generate_and_display_password)
generate_button.grid(column=0, row=2, pady=(5, 15))

password_display = ttk.Label(main_frame, text="", background='#2E3B4E', foreground='#ffffff')
password_display.grid(column=0, row=3, pady=(5, 15))

copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(column=0, row=4)

# Applying the background color to the main frame
main_frame.configure(style="TFrame")

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
