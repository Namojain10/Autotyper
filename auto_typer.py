import re
from pynput.keyboard import Controller
from tkinter import *
import tkinter as tk
import time
import keyboard as kb
import webbrowser
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./res")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = Tk()
#Windows Title
root.title("Auto Typer by Namo Jain")
root.geometry("600x400")
root.resizable(0,0)
root.configure(bg = "#FFFFFF")

#windows icon set
photo = PhotoImage(file="icons.png")

root.iconphoto(False, photo)


keyboard = Controller()

fontSmall= ('', 8)
cursor="hand2"
def callback(event):
    webbrowser.open_new_tab(event)

def rTime():
    time.sleep(4)
def rTime1():
    time.sleep(1)

def paste():
    input1=entry.get(1.0, tk.END+"-1c")
    rTime()
    keyboard.type(input1)

def paste1():
    input1=entry.get(1.0, tk.END+"-1c")
    rTime1()
    keyboard.type(input1)

def linebyline():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def singleline():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def linebyline1():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)

def singleline2():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)


canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    300.5,
    154.0,
    image=entry_image_1
)
entry = Text(
    bd=0,
    bg="#E6F0FF",
    highlightthickness=0
)
entry.place(
    x=19.0,
    y=6.0,
    width=563.0,
    height=294.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=paste,
    relief="flat"
)
button_1.place(
    x=246.0,
    y=324.0,
    width=95.0,
    height=35.0
)

kb.add_hotkey('ctrl+6', paste1)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=singleline,
    relief="flat"
)
button_2.place(
    x=362.0,
    y=323.0,
    width=95.0,
    height=37.30769348144531
)

kb.add_hotkey('ctrl+7', singleline2)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=linebyline,
    relief="flat"
)
button_3.place(
    x=474.0,
    y=324.0,
    width=113.0,
    height=35.0
)

kb.add_hotkey('ctrl+8', linebyline1)

canvas.create_text(
    6.0,
    389.0,
    anchor="nw",
    text="Version: 1.0.0",
    fill="#000000",
    font=("Microsoft Himalaya", 15 * -1)
)

canvas.create_text(
    440.0,
    388.0,
    anchor="nw",
    text="Auto Typing Software by Namo Jain",
    fill="#000000",
    font=("Microsoft Himalaya", 15 * -1)
)


canvas.create_text(
    279.0,
    360.0,
    anchor="nw",
    text="ctrl+6",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    396.0,
    360.0,
    anchor="nw",
    text="ctrl+7",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

canvas.create_text(
    510.0,
    360.0,
    anchor="nw",
    text="ctrl+8",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

lbl = Label(root, text="Github",fg='red',bg="white", highlightthickness=2,highlightbackground = "red", font=('', 20, 'bold'))
lbl.place(x=50, y=320)
lbl.bind("<Button>", lambda e: callback("https://bit.ly/sauravhathi"))

root.attributes('-topmost', True)

root.mainloop()