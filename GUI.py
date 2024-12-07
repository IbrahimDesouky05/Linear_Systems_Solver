# import tkinter as tk
#
# # Create the main window
# root = tk.Tk()
# root.title("Simple GUI")
# root.geometry("400x300")  # Set the size of the window
#
# # Add a label
# label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
# label.pack(pady=20)
#
# # Add an entry box
# entry = tk.Entry(root, width=30)
# entry.pack(pady=10)
#
# # Function for the button
# def on_button_click():
#     text = entry.get()
#     label.config(text=f"Hello, {text}!")
#
# # Add a button
# button = tk.Button(root, text="Click Me!", command=on_button_click)
# button.pack(pady=10)
#
# # Start the GUI event loop
# root.mainloop()
