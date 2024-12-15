import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk


def change_color(image):
    """ "
    This function change the color of the background,
    the size of the button and can make a image appear
    """

    global image_id

    color = "#%06x" % random.randint(0, 0xFFFFFF)
    button_width = random.randint(10, 15)
    button_height = random.randint(0, 5)

    root.config(bg=color)
    button1.place(x=random.randint(120, 520), y=random.randint(40, 440))

    button1.configure(width=button_width, height=button_height)

    if image_id == 0:
        if random.random() <= 0.2:
            image_label.config(image=image)
            image_id = 1
    else:
        image_label.config(image="")
        image_id = 0


def center():
    """ "
    This function lock the window width and height and set the window in the middle of the screen
    """

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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Joli fenêtre")
    root.config(bg="#%06x" % random.randint(0, 0xFFFFFF))

    center()

    root.resizable(False, False)  # Can not be resized
    root.attributes("-topmost", 1)  # Always on top of the stack order

    # Place a label on the root window

    message = ttk.Label(root, text="Appuie sur le button et je change de couleur")

    message.pack(padx=20, pady=20)

    # Read the Image
    global image_id

    image_id = 0
    image = Image.open("src/button/shrek.png")
    resize_image = image.resize((100, 100))
    img = ImageTk.PhotoImage(resize_image)

    image_label = ttk.Label(root, image="")
    image_label.pack()

    button1 = tk.Button(root, text="Cliquez moi", command=lambda: change_color(img))

    button1.place(x=320, y=240, anchor="center")

    # Keep the window displaying
    root.mainloop()
