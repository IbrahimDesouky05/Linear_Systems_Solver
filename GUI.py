import tkinter as tk

# Main window
root = tk.Tk()
root.title("Solving Linear System of Equations ")
root.geometry("1200x800")  # Set the size of the window

# Color Palette 
colors = {
    "background": "#F1F3F5",   # Light Gray
    "primary": "#007BFF",      # Blue
    "accent": "#20C997",       # Teal
    "text": "#343A40",         # Dark Gray
    "error": "#D32F2F",        # Red
}
root.configure(bg=colors["background"])

# Title Label
title_label = tk.Label(root,text="Solving Linear Systems",font=("Helvetica",25,"bold"),bg=colors["background"],fg=colors["primary"])
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root,font=("Helvetica",35), bg='white',fg=colors["text"],highlightbackground=colors["primary"],highlightthickness=2,width=50)
entry.pack(pady=10,padx=10)

# Test Function for the button
def on_button_click():
    text = entry.get()
    title_label.config(text=f"Hello, {text}!")

# Solve button
solve_button = tk.Button(root,text='Solve',font=("Helvetica",16),fg=colors["primary"],bg='white',activeforeground='white',activebackground=colors['primary'],relief='flat',highlightthickness=0, height=2,width=15,bd=(0),command=on_button_click,cursor='hand2')
solve_button.pack(pady=15)

# Error Label 
error_label = tk.Label(root,text='Invalid Input',font=("Helvetica",15),bg=colors['background'],fg=colors['error'])
error_label.pack(pady=5)
error_label.pack_forget() 
##
# Start the GUI event loop
root.mainloop()
