import tkinter as tk
from tkinter import messagebox
import MathFn as math
from math_helper_functions import invertibleMatrix
from output import create_pdf

# Define Colors
colors = {
    "background": "#F1F3F5",
    "primary": "#007BFF",
    "accent": "#20C997",
    "text": "#343A40",
    "error": "#D32F2F",
}

# Helper function to extract matrix values
def get_matrix_values(entry_fields, rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = entry_fields[i][j].get().strip()  # Get value and strip whitespace
            if value == "":  # Check for empty field
                messagebox.showerror("Input Error", f"Matrix field ({i+1}, {j+1}) is empty.")
                return None
            try:
                row.append(float(value))  # Convert value to integer
            except ValueError:
                messagebox.showerror("Input Error", f"Invalid value in matrix field ({i+1}, {j+1}).")
                return None
        matrix.append(row)
    return matrix

# Helper function to extract vector values
def get_vector_values(vector_fields, rows, title):

    vector = []
    for i in range(rows):
        value = vector_fields[i].get().strip()  # Get value and strip whitespace
        if value == "":  # Check for empty field
            messagebox.showerror("Input Error", f"{title} ({i+1}) is empty.")
            return None
        try:
            vector.append(float(value))  # Convert value to float
        except ValueError:
            messagebox.showerror("Input Error", f"Invalid value in vector field ({i+1}).")
            return None
    return vector

# Function to dynamically generate matrix input fields
def generate_matrix_fields(rows, cols):
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    global entry_fields
    entry_fields = []

    col = 0

    # Use grid for the label
    label = tk.Label(
        matrix_frame,
        text="Enter matrix (A):",
        font=("Helvetica", 12),
        bg=colors["background"]
    )
    label.grid(row=0, column=0, columnspan=cols, pady=5)

    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5, font=("Helvetica", 12), justify="center")
            entry.grid(row=i + 1, column=j, padx=2, pady=2)  # Shift rows down to leave space for the label
            row_entries.append(entry)
            col = j
        entry_fields.append(row_entries)
    return col

# Function to dynamically generate vector input fields
def generate_vector_fields(rows, col):
    for widget in vector_frame.winfo_children():
        widget.destroy()

    global vector_fields, strt_vector_fields
    vector_fields = []
    strt_vector_fields = []

    tk.Label(
        vector_frame,
        text="Enter the vector (b):",
        font=("Helvetica", 12),
        bg=colors["background"]
    ).pack(pady=5)

    tk.Label(
        strt_vector_frame,
        text="Enter initial conditions:",
        font=("Helvetica", 12),
        bg=colors["background"]
    ).pack(pady=5)

    for i in range(rows):
        entry = tk.Entry(vector_frame, width=5, font=("Helvetica", 12), justify="center")
        entry.pack(pady=2)
        vector_fields.append(entry)

        entry0 = tk.Entry(strt_vector_frame, width=5, font=("Helvetica", 12), justify="center")
        entry0.pack(pady=2)
        strt_vector_fields.append(entry0)

# Function to generate both matrix and vector fields
def generate_input_fields():
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
        if rows != cols:
            messagebox.showerror("Input Error", "Only square matrices are allowed (e.g., 3x3, 4x4).")
            return
    except ValueError:
        result_label.config(text="Invalid size input. Enter numbers only.")
        return

    clear_frame(ans_frame)
    clear_frame(strt_vector_frame)
    col = generate_matrix_fields(rows, cols)
    generate_vector_fields(rows, 0)
    generate_solve_button()

# Function to generate solve button
def generate_solve_button():
    # Solve Button
    solve_button = tk.Button(
        root,
        text="Solve",
        bg=colors["primary"],
        fg="white",
        font=("Helvetica", 12, "bold"),
        command=handle_solve
    )
    solve_button.pack(pady = 20)

# Function to handle Submit button action
def handle_solve():

    size = int(rows_entry.get())

    # Retrieve matrix and vector values
    matrix = get_matrix_values(entry_fields, size, size)
    vector = get_vector_values(vector_fields, size,"Answer Vector")
    start_vector = get_vector_values(strt_vector_fields, size, "Starting Vector")

    if invertibleMatrix(matrix):
        messagebox.showerror("Input Error", "Matrix is Non-invertible.")
        return

    if vector == None:
        # Replaced by a previous check
        # messagebox.showerror("Input Error", "No vector was entered.")
        return
    if start_vector == None:
        return

    # Display or process the submitted values
    # print("Matrix Submitted:", matrix)        # Used in debugging
    # print("Vector Submitted:", vector)        # Used in debugging
    result_label.config(text="Matrix and Vector submitted successfully!", fg=colors["text"])
    ans1, ans2, ans3, ans4, i1, i2, t1, t2, t3, t4 = math.all_math_functions(matrix, vector, size)
    #clear_frame(vector_frame)
    clear_frame(ans_frame)
    clear_frame(result_label)

    display_vector_in_column(ans_frame, "Gaussian Elimination:", ans1, 0)
    display_vector_in_column(ans_frame, "LU Decomposition:", ans2, 2)
    display_vector_in_column(ans_frame, "Gauss Seidel:", ans3, 4)
    end = display_vector_in_column(ans_frame, "Jacobian:", ans4, 6) + 1

    display_value(ans_frame, "Time (ms):", t1, end, 0)
    display_value(ans_frame, "Time (ms):", t2, end, 2)
    display_value(ans_frame, "Time (ms):", t3, end, 4)
    display_value(ans_frame, "Time (ms):", t4, end, 6)

    display_value(ans_frame, "Iterations:", i1, end + 1, 4)
    display_value(ans_frame, "Iterations:",i2, end + 1, 6)

    sol = [ans1, ans2, ans3, ans4]

    methods = {
        "Gauss Elimination": {"time": t1, "iterations": 0},
        "LU Decomposition": {"time": t2, "iterations": 0},
        "Gauss Seidel": {"time": t3, "iterations": i1},
        "Jacobian": {"time": t4, "iterations": i2}
    }

    create_pdf("Matrix Solution Report.pdf",matrix,vector,sol,methods,start_vector)

# Function to clear the given frame
def clear_frame(parent_frame):
    # Clear the parent frame
    for widget in parent_frame.winfo_children():
        widget.destroy()

# Function to display the given vector
def display_vector_in_column(parent_frame, label, vector, col):

    # Clear the parent frame
    #  for widget in parent_frame.winfo_children():
    #      widget.destroy()

    length = len(vector)

    # Display the main vector label
    tk.Label(
        parent_frame,
        text=f"{label}:",
        font=("Helvetica", 12, "bold"),
        bg=colors["background"],
        anchor="w"
    ).grid(row = length, column = col, padx=10, pady=5, sticky="w")

    # Display each element in the vector
    for idx, value in enumerate(vector):
        tk.Label(
            parent_frame,
            text=f"X ({idx}):",
            font=("Helvetica", 12),
            bg=colors["background"],
            anchor="w"
        ).grid(row=idx + length + 1, column = col, padx=10, pady=5, sticky="w")

        tk.Label(
            parent_frame,
            text=str(value),
            font=("Helvetica", 12),
            bg=colors["background"],
            fg=colors["text"]
        ).grid(row=idx + length + 1, column = col + 1, padx=10, pady=5, sticky="w")
        row = idx + length + 1
    return row

# Function to display the given value
def display_value(parent_frame, title,val, row, col):

    tk.Label(
        parent_frame,
        text=title,
        font=("Helvetica", 12),
        bg=colors["background"],
        anchor="w"
    ).grid(row = row, column = col, padx=10, pady=5, sticky="w")

    tk.Label(
        parent_frame,
        text=str(val),
        font=("Helvetica", 12),
        bg=colors["background"],
        fg=colors["text"]
    ).grid(row = row, column = col + 1, padx=10, pady=5, sticky="w")

# Function to set up the main GUI
def setup_gui(root):
    root.title("Solving Linear System")
    root.geometry("1000x700")
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

    global rows_entry, cols_entry
    tk.Label(input_frame, text="Rows:", font=("Helvetica", 12), bg=colors["background"]).grid(row=0, column=0)
    rows_entry = tk.Entry(input_frame, width=5, font=("Helvetica", 12), justify="center")
    rows_entry.grid(row=0, column=1, padx=10)

    tk.Label(input_frame, text="Columns:", font=("Helvetica", 12), bg=colors["background"]).grid(row=0, column=2)
    cols_entry = tk.Entry(input_frame, width=5, font=("Helvetica", 12), justify="center")
    cols_entry.grid(row=0, column=3, padx=10)

    generate_button = tk.Button(
        input_frame,
        text="Generate Inputs",
        bg=colors["accent"],
        fg="white",
        command=generate_input_fields
    )
    generate_button.grid(row=0, column=4, padx=10)

    global matrix_frame, vector_frame, result_label, ans_frame, strt_vector_frame

    # Frames for Matrix and Vector Input
    matrix_frame = tk.Frame(root, bg=colors["background"])
    matrix_frame.pack(pady=10)

    vector_frame = tk.Frame(root, bg=colors["background"])
    vector_frame.pack(pady=10)

    strt_vector_frame = tk.Frame(root, bg=colors["background"])
    strt_vector_frame.pack(pady=10)

    ans_frame = tk.Frame(root, bg=colors["background"])
    ans_frame.pack(pady=10)

    # Made as a function
    # # Submit Button
    # solve_button = tk.Button(
    #     root,
    #     text="Solve",
    #     bg=colors["primary"],
    #     fg="white",
    #     font=("Helvetica", 12, "bold"),
    #     command=handle_solve
    # )
    # solve_button.pack(pady = 20)

    # Made as a function
    # # Pdf Button
    # pdf_button = tk.Button(
    #     root,
    #     text="Create PDF",
    #     bg=colors["primary"],
    #     fg="white",
    #     font=("Helvetica", 12, "bold"),
    #     command=handle_solve
    # )
    # pdf_button.pack(pady=20)

    # Result Label
    result_label = tk.Label(
        root,
        text="",
        font=("Helvetica", 12),
        bg=colors["background"],
        fg=colors["error"]
    )
    result_label.pack()

# def get_matrix_and_vector():
#     """
#     Retrieves the values of the matrix and vector from the input fields.
#
#     Returns:
#         tuple: A tuple containing two elements:
#             - matrix (list of lists): The 2D list representing the matrix.
#             - vector (list): The list representing the vector.
#     """
#     try:
#         rows = int(rows_entry.get())
#         cols = int(cols_entry.get())
#         if rows != cols:
#             messagebox.showerror("Input Error", "Only square matrices are allowed (e.g., 3x3, 4x4).")
#             return None, None
#     except ValueError:
#         messagebox.showerror("Input Error", "Invalid size input. Enter numbers only.")
#         return None, None
#
#     # Retrieve matrix and vector values
#     matrix = get_matrix_values(entry_fields, rows, cols)
#     vector = get_vector_values(vector_fields, rows)
#
#     print("Matrix Retrieved:", matrix)
#     print("Vector Retrieved:", vector)
#
#     return matrix, vector, rows



# Main Function
def main():
    global root
    root = tk.Tk()
    setup_gui(root)
    root.mainloop()
