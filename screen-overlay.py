import tkinter as tk
from tkinter import colorchooser

# Function to move the window when dragged
def on_drag(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

# Function to resize the window when dragged at the edges
def start_resize(event):
    global x, y, width, height
    x = event.x
    y = event.y
    width = root.winfo_width()
    height = root.winfo_height()

def do_resize(event):
    dx = event.x - x
    dy = event.y - y
    new_width = max(root.minsize()[0], width + dx)
    new_height = max(root.minsize()[1], height + dy)
    root.geometry(f'{new_width}x{new_height}')

# Change button colors to match the background when mouse leaves
def hide_buttons(event):
    close_button.config(bg=frame.cget("bg"), fg=frame.cget("bg"), activebackground=frame.cget("bg"))
    resize_handle.config(bg=frame.cget("bg"))
    color_picker_button.config(bg=frame.cget("bg"))

# Restore the original button colors when mouse enters
def show_buttons(event):
    close_button.config(bg="red", fg="white", activebackground="darkred")
    resize_handle.config(bg="blue")
    color_picker_button.config(bg=frame.cget("bg"), fg="black", activebackground="lightgray")

# Function to open a color picker and change window background
def pick_color():
    color = colorchooser.askcolor()[1]  # Get the hex code of the selected color
    if color:
        frame.config(bg=color)  # Change the background of the window to the selected color
        color_picker_button.config(bg=color)  # Change the color picker button to match the window

# Create the main window
root = tk.Tk()

# Remove window decorations (title bar, border, etc.)
root.overrideredirect(True)

# Set minimum size for resizing
root.minsize(200, 100)

# Create a frame for the window's content area
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

# Bind dragging to the frame
frame.bind("<B1-Motion>", on_drag)

# Create a close button that blends with the window when hidden
close_button = tk.Button(frame, text="X", command=root.quit, bg="red", fg="white", borderwidth=0)

# Create a resize handle in the bottom-right corner
resize_handle = tk.Frame(root, bg="blue", cursor="bottom_right_corner", width=10, height=10)
resize_handle.bind("<Button-1>", start_resize)
resize_handle.bind("<B1-Motion>", do_resize)

# Add a color picker button in the top-left corner
color_picker_button = tk.Button(frame, text="🎨", command=pick_color, bg="lightblue", fg="black", borderwidth=0)
color_picker_button.place(relx=0.0, rely=0.0, anchor="nw")

# Bind mouse enter and leave events to change button colors
frame.bind("<Enter>", show_buttons)
frame.bind("<Leave>", hide_buttons)

# Place buttons initially (you can start with hidden colors if preferred)
close_button.place(relx=1.0, rely=0.0, anchor="ne")
resize_handle.place(relx=1.0, rely=1.0, anchor="se")

# Run the main loop
root.mainloop()
