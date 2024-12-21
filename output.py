from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.colors import black
from datetime import datetime
import os

def create_header(c, width, height):
    """Creates a fancy header for the PDF."""
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.blue)
    c.drawString(50, height - 50, "Matrix Problem Report")

    # Draw a line beneath the header
    c.setStrokeColor(colors.blue)
    c.setLineWidth(1.5)
    c.line(50, height - 55, width - 50, height - 55)

    # Subheading with the current date
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    current_date = datetime.now().strftime("%B %d, %Y")
    c.drawString(50, height - 70, f"Generated on: {current_date}")

def create_footer(c, width, page_num):
    """Creates a footer for the PDF."""
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.grey)
    c.drawString(50, 25, page_num)
    c.drawString(475, 25, "Dr Amani Elgammal")
    c.setFillColor(colors.grey)
    c.line(50, 45, width - 50, 45)  # Footer line

def draw_matrix(c, matrix, start_x, start_y):
    """Draws a matrix with brackets on the PDF."""
    c.setFont("Helvetica", 12)
    c.setFillColor(black)
    c.drawString(start_x - 50, start_y + 10, "Matrix (A):")
    c.line(start_x - 50, start_y + 10 - 5, start_x + len("Matrix (A):") - 5, start_y + 10 - 5)

    shit_y = -25

    # Draw opening bracket
    c.line(start_x - 10, start_y + 10 + shit_y, start_x - 10, start_y - (len(matrix) * 15) - 10 + shit_y)
    c.line(start_x - 10, start_y + 10 + shit_y, start_x - 5, start_y + 10 + shit_y)
    c.line(start_x - 10, start_y - (len(matrix) * 15) - 10 + shit_y, start_x - 5, start_y - (len(matrix) * 15) - 10 + shit_y)

    # Draw closing bracket
    closing_x = start_x + (len(matrix[0]) * 50)
    c.line(closing_x, start_y + 10 + shit_y, closing_x, start_y - (len(matrix) * 15) - 10 + shit_y)
    c.line(closing_x, start_y + 10 + shit_y, closing_x - 5, start_y + 10 + shit_y)
    c.line(closing_x, start_y - (len(matrix) * 15) - 10 + shit_y, closing_x - 5, start_y - (len(matrix) * 15) - 10 + shit_y)

    end_y =  start_y - (len(matrix) * 15) - 10 + shit_y

    # Draw matrix content
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            c.drawString(start_x + 10 + j * 50, start_y - 5 - i * 20 + shit_y, f"{value}")

    return end_y - 40

def draw_vector(c, vector, start_x, start_y, title):
    """Draws a vector on the PDF."""

    shift_x = 20
    shift_y = -25

    end_vect = 0

    # Draw opening bracket
    c.line(start_x + 65, start_y + 10 + shift_y, start_x + 65, start_y - (len(vector) * 15) - 10 + shift_y)
    c.line(start_x + 65, start_y + 10 + shift_y, start_x + 70, start_y + 10 + shift_y)
    c.line(start_x + 65, start_y - (len(vector) * 15) - 10 + shift_y, start_x + 70, start_y - (len(vector) * 15) - 10 + shift_y)

    # Draw closing bracket
    closing_x = start_x + 90
    c.line(closing_x + shift_x, start_y + 10 + shift_y, closing_x + shift_x, start_y - (len(vector) * 15) - 10 + shift_y)
    c.line(closing_x + shift_x, start_y + 10 + shift_y, closing_x - 5 + shift_x, start_y + 10 + shift_y)
    c.line(closing_x + shift_x, start_y - (len(vector) * 15) - 10 + shift_y, closing_x - 5 + shift_x, start_y - (len(vector) * 15) - 10 + shift_y)

    c.setFont("Helvetica", 12)
    c.setFillColor(black)
    c.drawString(start_x, start_y + 10 , title)
    c.line(start_x, start_y + 10 - 5, start_x + (len(title) * 4.8), start_y + 10 - 5)
    # Draw vector content
    for i, val in enumerate(vector):
        c.drawString(start_x + 75, start_y - 5 - i * 20 + shift_y, f"{val}")
        end_vect =  start_y - 5 - i * 20 + shift_y

    return end_vect

def draw_solutions_table(c, start_x, start_y, width, height, solutions, methods):
    # Set the font and title for the table
    c.setFont("Helvetica", 12)
    c.setFillColor(black)
    c.drawString(start_x - 25, start_y, "Solutions:")
    c.line(start_x - 25, start_y - 5, start_x + len("Solutions") + 25, start_y - 5)

    # Create the header row for the table
    table_data = [["Method", "Solution (Vector)", "Time (ms)", "Iterations"]]

    # Get the methods in the same order as the solutions
    method_names = list(methods.keys())

    # Iterate over solutions and methods in the given order
    for i, solution_vector in enumerate(solutions):
        method = method_names[i]  # Get the method corresponding to this solution
        method_data = methods[method]  # Get time and iterations for this method

        # Initialize an empty list to store formatted numbers
        formatted_numbers = []

        # Iterate over each element in the solution vector and format it
        for x in solution_vector:
            try:
                # Attempt to convert to float and format with high precision
                num = float(x)
                formatted_numbers.append(f'{num:.6f}')  # Format with up to 6 decimal places
            except ValueError:
                # Handle the case where conversion fails (e.g., non-numeric value)
                print(f"Warning: Non-numeric value '{x}' encountered in solution vector for method '{method}'.")
                formatted_numbers.append(str(x))  # Append as string if not numeric

        # Join the formatted numbers into a string
        solution_str = ', '.join(formatted_numbers)

        # Format time as float with 4 decimal places
        time_str = f'{float(method_data["time"]):.4f}'

        # Append the row to the table
        table_data.append([
            method,                     # Method name
            solution_str,               # Solution as a formatted string
            time_str,                   # Time formatted to 4 decimal places
            method_data["iterations"]   # Number of iterations as integer
        ])

    # Create a table object with fixed column widths
    col_widths = [150, 175, 75, 75]
    table = Table(table_data, colWidths=col_widths)

    # Apply styles to the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.aliceblue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),       # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),              # Center-align all cells
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),    # Bold font for header
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),             # Extra padding for header
        ('GRID', (0, 0), (-1, -1), 1, colors.black),        # Gridlines for all cells
    ]))

    # Draw the table on the canvas
    table.wrapOn(c, width, height)
    table.drawOn(c, start_x, start_y - 125)

def draw_image(c,file_name, x, y, width, height):

    image_path = file_name  # Assuming the image is in the same directory as the script

    c.drawImage(image_path, x, y, width, height)

def create_pdf(file_name, matrix, vector, solutions, methods, inital_conditions):

    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Add components
    create_header(c, width, height)
    create_footer(c, width, "Page 1")
    end_y = draw_matrix(c, matrix, 100, height - 120)
    draw_vector(c, vector, 400, height - 120, "Vector (b): ")
    end_vector = draw_vector(c, inital_conditions, 50,end_y - 20,"Initial conditions:")
    draw_solutions_table(c, 75, end_vector - 80, width, height, solutions, methods)


    c.showPage()
    create_header(c, width, height)
    create_footer(c, width, "Page 2")
    draw_image(c, "Convergence of Gauss-Seidel Method.png", 100, height - 400, 400, 300)
    draw_image(c, "Convergence of Jacobian Method.png", 100, 100, 400, 300)

    # Save the PDF
    c.save()
    os.startfile(file_name)


# matrix = [
#     [3, -1, 2],
#     [2, 4, 1],
#     [5, -3, 3]
# ]
#
# # Example solution vector (3x1)
# vector = [1.0, 2.5, -0.5]
#
# # Example solution vectors for 4 methods
# solutions = [
#         [1.0, 2.5, -0.5],
#         [0.5, 1.0, -0.2],
#         [2.0, -1.5, 3.0],
#         [3.5, -0.5, 2.0]
# ]
#
# # Example methods metadata
# methods = {
#     "Gauss Elimination": {"time": 0.025, "iterations": 100},
#     "LU Decomposition": {"time": 0.030, "iterations": 120},
#     "Gauss Seidel": {"time": 0.020, "iterations": 90},
#     "Jacobian": {"time": 0.035, "iterations": 110}
# }
#
# Generate the PDF
# create_matrix_pdf("Matrix Solution Report.pdf", matrix, vector, solutions, methods)