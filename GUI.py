import tkinter as tk
from tkinter import messagebox 

# Helper function to convert matrix input from string to integer
def get_matrix_values(entry_fields, rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            try:
                value = int(entry_fields[i][j].get())  
                row.append(value)
            except ValueError:
                row.append(0) 
        matrix.append(row)
    print("Matrix:", matrix) 
    return matrix

# Function to generate matrix input fields dynamically
def generate_matrix_fields():
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
        
        # Validation for square matrices
        if rows != cols:
            messagebox.showerror("Input Error", "Only square matrices are allowed (e.g., 3x3, 4x4).")
            return
    except ValueError:
        result_label.config(text="Invalid size input. Enter numbers only.")
        return

    for widget in matrix_frame.winfo_children():
        widget.destroy()

    global entry_fields
    entry_fields = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5, font=("Helvetica", 12), justify="center")
            entry.grid(row=i, column=j, padx=2, pady=2)
            row_entries.append(entry)
        entry_fields.append(row_entries)

    submit_button = tk.Button(
        matrix_frame,
        text="Submit Matrix",
        bg=colors["accent"],
        fg="white",
        command=lambda: get_matrix_values(entry_fields, rows, cols)
    )
    submit_button.grid(row=rows, column=0, columnspan=cols, pady=10)

# Main Tkinter Window
root = tk.Tk()
root.title("Solving Linear System")
root.geometry("1000x700")

# Define Colors
colors = {
    "background": "#F1F3F5",
    "primary": "#007BFF",
    "accent": "#20C997",
    "text": "#343A40",
    "error": "#D32F2F",
}

root.configure(bg=colors["background"])

# Title Label
title_label = tk.Label(
    root,
    text="Solving Linear Systems",
    font=("Helvetica", 16, "bold"),
    bg=colors["background"],
    fg=colors["primary"]
)
title_label.pack(pady=10)

# Input Section for Rows and Columns
input_frame = tk.Frame(root, bg=colors["background"])
input_frame.pack(pady=10)

tk.Label(input_frame, text="Rows:", font=("Helvetica", 12), bg=colors["background"]).grid(row=0, column=0)
rows_entry = tk.Entry(input_frame, width=5, font=("Helvetica", 12))
rows_entry.grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Columns:", font=("Helvetica", 12), bg=colors["background"]).grid(row=0, column=2)
cols_entry = tk.Entry(input_frame, width=5, font=("Helvetica", 12))
cols_entry.grid(row=0, column=3, padx=10)

generate_button = tk.Button(
    input_frame,
    text="Generate Matrix",
    bg=colors["accent"],
    fg="white",
    command=generate_matrix_fields
)
generate_button.grid(row=0, column=4, padx=10)

matrix_frame = tk.Frame(root, bg=colors["background"])
matrix_frame.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    bg=colors["background"],
    fg=colors["error"]
)
result_label.pack()

root.mainloop()
