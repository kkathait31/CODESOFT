import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title(" CALCULATOR")

# Entry widget for display
entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12), command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 12), command=clear_entry).grid(row=row_val, column=col_val)

# Run the application
root.mainloop()
