import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# -------------------------
# Password Generator
# -------------------------

def generate_password():
    try:
        length = int(length_var.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror(
                "Error",
                "Select at least one character type."
            )
            return

        password = ""

        # Ensure every selected type appears at least once
        mandatory = []

        if uppercase_var.get():
            mandatory.append(random.choice(string.ascii_uppercase))

        if lowercase_var.get():
            mandatory.append(random.choice(string.ascii_lowercase))

        if numbers_var.get():
            mandatory.append(random.choice(string.digits))

        if symbols_var.get():
            mandatory.append(random.choice(string.punctuation))

        if length < len(mandatory):
            messagebox.showerror(
                "Error",
                f"Minimum length should be {len(mandatory)}."
            )
            return

        password = mandatory

        password += random.choices(
            characters,
            k=length - len(mandatory)
        )

        random.shuffle(password)

        password = "".join(password)

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

        update_strength(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")


# -------------------------
# Password Strength
# -------------------------

def update_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(
            text="Weak",
            foreground="red"
        )

    elif score == 3 or score == 4:
        strength_label.config(
            text="Medium",
            foreground="orange"
        )

    else:
        strength_label.config(
            text="Strong",
            foreground="green"
        )


# -------------------------
# Copy Password
# -------------------------

def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


# -------------------------
# Clear
# -------------------------

def clear_all():

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

    strength_label.config(
        text="Not Generated",
        foreground="blue"
    )


# -------------------------
# GUI
# -------------------------

root = tk.Tk()
root.title("Password Generator")
root.geometry("520x470")
root.resizable(False, False)
root.configure(bg="#F4F6F9")

title = tk.Label(
    root,
    text="Secure Password Generator",
    font=("Arial", 20, "bold"),
    bg="#F4F6F9",
    fg="#2C3E50"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Length

tk.Label(
    frame,
    text="Password Length",
    font=("Arial", 12),
    bg="white"
).pack(pady=(20, 5))

length_var = tk.StringVar(value="12")

length_spin = tk.Spinbox(
    frame,
    from_=4,
    to=50,
    textvariable=length_var,
    width=10,
    font=("Arial", 12)
)
length_spin.pack()

# Checkboxes

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Checkbutton(
    frame,
    text="Uppercase Letters",
    variable=uppercase_var
).pack(anchor="w", padx=30, pady=4)

ttk.Checkbutton(
    frame,
    text="Lowercase Letters",
    variable=lowercase_var
).pack(anchor="w", padx=30, pady=4)

ttk.Checkbutton(
    frame,
    text="Numbers",
    variable=numbers_var
).pack(anchor="w", padx=30, pady=4)

ttk.Checkbutton(
    frame,
    text="Symbols",
    variable=symbols_var
).pack(anchor="w", padx=30, pady=4)

# Buttons

button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=15)

generate_btn = tk.Button(
    button_frame,
    text="Generate",
    command=generate_password,
    bg="#27AE60",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
)

generate_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    bg="#E74C3C",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
)

clear_btn.grid(row=0, column=1)

# Password Box

tk.Label(
    frame,
    text="Generated Password",
    bg="white",
    font=("Arial", 12)
).pack()

password_entry = tk.Entry(
    frame,
    font=("Consolas", 13),
    width=35,
    justify="center",
    state="readonly"
)

password_entry.pack(pady=10)

copy_btn = tk.Button(
    frame,
    text="Copy Password",
    command=copy_password,
    bg="#3498DB",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
)

copy_btn.pack(pady=5)

# Strength

strength_text = tk.Label(
    frame,
    text="Password Strength",
    bg="white",
    font=("Arial", 12, "bold")
)

strength_text.pack(pady=(15, 0))

strength_label = tk.Label(
    frame,
    text="Not Generated",
    bg="white",
    fg="blue",
    font=("Arial", 13, "bold")
)

strength_label.pack(pady=5)

footer = tk.Label(
    root,
    text="Made with Python & Tkinter",
    bg="#F4F6F9",
    fg="gray"
)

footer.pack(pady=10)

root.mainloop()

