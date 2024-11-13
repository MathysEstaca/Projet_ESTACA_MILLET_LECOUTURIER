import tkinter
import random

def change_color():
    color = "#%06x" %random.randint(0, 0xFFFFFF)
    fenetre.config(bg = color)

fenetre = tkinter.Tk()
fenetre.title("Joli fenêtre")
fenetre.geometry("640x480")
texte1 = tkinter.Label(fenetre, text = "Appuie sur le bouton et je change de couleur")
texte1.pack()
bouton1 = tkinter.Button(fenetre, text = "Cliquez moi", command=change_color)
bouton1.pack(side="left")
fenetre.mainloop()