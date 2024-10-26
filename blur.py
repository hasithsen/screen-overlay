import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk
import mss

# Create the main application window
root = tk.Tk()
root.attributes('-topmost', True)
root.geometry("800x600")  # Size of the overlay window
root.overrideredirect(True)  # Remove the title bar for a frameless window

# Label to hold the blurred screenshot
label = tk.Label(root)
label.pack()

# Capture and continuously update the screen with a blur
def update_image():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary monitor
        img = np.array(sct.grab(monitor))

    # Apply blur
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.GaussianBlur(img, (21, 21), 0)

    # Convert image for Tkinter and display it
    imgtk = ImageTk.PhotoImage(image=Image.fromarray(img))
    label.imgtk = imgtk
    label.configure(image=imgtk)
    root.after(50, update_image)  # Update every 50 ms

update_image()
root.mainloop()
