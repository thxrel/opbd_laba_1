import tkinter as tk
import random
import string

def generate_password():
    length = int(length_var.get())
    use_letters = letters_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Пароль: {password}")

root = tk.Tk()
root.title("Генератор Паролей")

length_label = tk.Label(root, text="Длина пароля:")
length_label.grid(row=0, column=0)
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.grid(row=0, column=1)

letters_var = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(root, text="Использовать буквы", variable=letters_var)
letters_checkbox.grid(row=1, column=0)
digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Использовать цифры", variable=digits_var)
digits_checkbox.grid(row=1, column=1)
symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Использовать символы", variable=symbols_var)
symbols_checkbox.grid(row=1, column=2)

generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=3)

result_label = tk.Label(root, text="Пароль:")
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()