import tkinter as tk
import math

# Function to perform calculations
def calculate(operation=None):
    try:
        expression = result_var.get()
        if operation == 'equal':
            result = eval(expression)
            result_var.set(str(result))
        elif operation == 'clear':
            result_var.set('')
        elif operation == 'square':
            result = eval(expression) ** 2
            result_var.set(str(result))
        elif operation == 'sqrt':
            result = math.sqrt(eval(expression))
            result_var.set(str(result))
        else:
            result_var.set(expression + operation)
    except Exception:
        result_var.set('Error')

# Setting up the window
root = tk.Tk()
root.title('Enhanced Calculator')
root.geometry('320x450')
root.resizable(False, False)
root.configure(bg='#2C2F33')

# Entry widget for the result (Top)
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=('Arial', 18), bd=10, insertwidth=2, width=16, borderwidth=4, justify='right', bg='#23272A', fg='white')
result_entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button Styles
def create_button(text, row, col, bg_color, fg_color, command=None):
    return tk.Button(root, text=text, padx=20, pady=15, font=('Arial', 12), bg=bg_color, fg=fg_color, activebackground='#7289DA', command=command).grid(row=row, column=col)

# Buttons Configuration
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3, '+'),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3, '-'),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3, '*'),
    ('0', 4, 0), ('C', 4, 1, 'clear'), ('=', 4, 2, 'equal'), ('/', 4, 3, '/'),
    ('x²', 5, 0, 'square'), ('√x', 5, 1, 'sqrt')
]

for (text, row, col, *operation) in button_texts:
    if operation:
        action = lambda op=operation[0]: calculate(op)
    else:
        action = lambda text=text: result_var.set(result_var.get() + text)

    bg_color = '#99AAB5' if text.isdigit() else '#7289DA'
    fg_color = 'black' if text.isdigit() else 'white'
    create_button(text, row, col, bg_color, fg_color, command=action)

root.mainloop()
