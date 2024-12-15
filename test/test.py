# from src.button import main

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

def change_color():
    global image_id

    if image_id == 0:
        image_id = 1
    else:
        image_id = 0

def test1():
    global image_id
    image_id = 0
    change_color()
    assert image_id == 1

def test2():
    global image_id
    image_id = 1
    change_color()
    assert image_id == 0