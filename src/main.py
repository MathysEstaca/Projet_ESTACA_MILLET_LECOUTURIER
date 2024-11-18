import tkinter as tk
import random

def change_color():
    global image_id

    if image_id == None:
        if random.random() <= 0.2:
            image_label = tk.Label(root, image=image)
            image_label.pack()
    else:
        image_label.pack_forget()
        image_id = None

    color = "#%06x" %random.randint(0, 0xFFFFFF)
    root.config(bg = color)
    bouton1.place(x=random.randint(0, 640), y=random.randint(0, 480))


# TODO the bouton!!!!

image_id = None

root = tk.Tk()
root.title("Joli fenêtre")

window_width = 640
window_height = 480

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

# Place a label on the root window
message = tk.Label(root, text = "Appuie sur le bouton et je change de couleur")
message.pack()

# Load the image 
image = tk.PhotoImage(file="shrek.png")

bouton1 = tk.Button(root, text = "Cliquez moi", command=change_color)
bouton1.place(x=0, y=0)
root.config(bg = "#%06x" %random.randint(0, 0xFFFFFF))

# Keep the window displaying
root.mainloop()