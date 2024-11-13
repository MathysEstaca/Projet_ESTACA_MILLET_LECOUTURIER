import tkinter
import random

def change_color():
    color = "#%06x" %random.randint(0, 0xFFFFFF)
    fenetre.config(bg = color)
    bouton1.place(x=random.randint(0, 640), y=random.randint(0, 480)) 


fenetre = tkinter.Tk()
fenetre.title("Joli fenêtre")
fenetre.geometry("640x480")
texte1 = tkinter.Label(fenetre, text = "Appuie sur le bouton et je change de couleur")
texte1.pack()
bouton1 = tkinter.Button(fenetre, text = "Cliquez moi", command=change_color)
bouton1.place(x=640, y=480)
fenetre.config(bg = "#%06x" %random.randint(0, 0xFFFFFF))
fenetre.mainloop()