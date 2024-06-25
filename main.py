import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

root = tk.Tk()
root.title("Password Generator")
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

def generate_and_display_password():
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    password_display.config(text=password)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()
password_display = tk.Label(root, text="")
password_display.pack()
root.mainloop()