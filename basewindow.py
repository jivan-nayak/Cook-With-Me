from tkinter import *
import GUI
import webbrowser

class base(self, title):
    def __init__(self) -> None:
        super().__init__()
        master = Tk()
        master.attributes("-fullscreen",True)
        master.title(title)