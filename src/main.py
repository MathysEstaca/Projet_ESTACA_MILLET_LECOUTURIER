import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


def change_color():
    global image_id

    color = "#%06x" % random.randint(0, 0xFFFFFF)
    root.config(bg=color)
    bouton1.place(x=random.randint(120, 520), y=random.randint(40, 440))

    if image_id == None:
        if random.random() <= 0.2:
            image_label = ttk.Label(root, image=img)
            image_label.pack()
            image_id = 1
    else:
        image_label.pack_forget()
        image_id = None


def center():
    window_width = 640
    window_height = 480

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# TODO the bouton!!!!

image_id = None

root = tk.Tk()
root.title("Joli fenêtre")
root.config(bg="#%06x" % random.randint(0, 0xFFFFFF))

center()

root.resizable(False, False)  # Can not be resized
root.attributes("-topmost", 1)  # Always on top of the stack order

# Place a label on the root window
message = ttk.Label(root, text="Appuie sur le bouton et je change de couleur")

message.pack(padx=20, pady=20)


# Read the Image
image = Image.open("shrek.png")
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)

bouton1 = ttk.Button(root, text="Cliquez moi", command=change_color)

bouton1.place(x=320, y=240, anchor="center")

# Keep the window displaying
root.mainloop()
