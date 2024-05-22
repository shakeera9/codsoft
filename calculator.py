import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
tk.Label(root, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create radio buttons for operations
var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]

for i, operation in enumerate(operations):
    tk.Radiobutton(root, text=operation, variable=var, value=operation).grid(row=2+i, column=0, columnspan=2)

# Create a button to perform the calculation
tk.Button(root, text="Calculate", command=calculate).grid(row=6, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=7, column=0, columnspan=2)

# Run the application
root.mainloop()
