import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    def calculate():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
        except ValueError:
            result_label.config(text="Invalid input. Please enter numeric values.")
            return

        choice = choice_var.get()

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            result = "Invalid input. Please enter a valid choice."

        result_label.config(text="Result: " + str(result))

    root = tk.Tk()
    root.title("Calculator")

    choice_var = tk.StringVar(root, '1')

    label_num1 = tk.Label(root, text="Enter first number:")
    label_num1.grid(row=0, column=0)
    entry_num1 = tk.Entry(root)
    entry_num1.grid(row=0, column=1)

    label_num2 = tk.Label(root, text="Enter second number:")
    label_num2.grid(row=1, column=0)
    entry_num2 = tk.Entry(root)
    entry_num2.grid(row=1, column=1)

    label_choice = tk.Label(root, text="Select operation:")
    label_choice.grid(row=2, column=0)
    option_menu = tk.OptionMenu(root, choice_var, '1', '2', '3', '4')
    option_menu.grid(row=2, column=1)

    calculate_button = tk.Button(root, text="Calculate", command=calculate)
    calculate_button.grid(row=3, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()

calculator()
