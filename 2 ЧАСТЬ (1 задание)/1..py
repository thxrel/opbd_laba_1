import tkinter as tk


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        label_result.config(text=str(result))
    except ValueError:
        label_result.config(text="ошибка")


root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

operation_var = tk.StringVar()
operation_var.set("+")

operation_buttons = [
    ("+", "+"),
    ("-", "-"),
    ("*", "*"),
    ("/", "/")
]

for text, value in operation_buttons:
    button = tk.Radiobutton(root, text=text, variable=operation_var, value=value)
    button.pack(side="left")

calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()

