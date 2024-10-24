import tkinter as tk
from tkinter import messagebox

def sum_integers(input_list):
    total = 0
    for item in input_list:
        if isinstance(item, int):
            total += item
    return total

def calculate():
    input_data = entry.get().split(',')
    integers = [int(x) for x in input_data if x.strip().isdigit()]
    result = sum_integers(integers)
    messagebox.showinfo("Result", f"The sum of all integers is: {result}")

# Create the main window
root = tk.Tk()
root.title("Sum Integers App")

# Create and place the widgets
label = tk.Label(root, text="Enter variables and integers (separated by commas):")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Start the main loop
root.mainloop()
