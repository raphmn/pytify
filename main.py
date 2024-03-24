import customtkinter as ctk
import tkinter as tk

from PIL import Image
import ctypes

from app.player_frame import *
from app.navigator import *

applicationID = 'nsi.project.spotify.1_0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(applicationID)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x500')
        self.title('Spotify')
        self.iconbitmap('media/appicon/appicon.ico')

        self.navigator = LateralFrame(self, width=180, height=500)
        self.navigator.pack(anchor=tk.NW, side="left")

        self.player_bar = PlayerFrame(self, width=820, height=50)
        self.player_bar.pack(anchor="s", side="bottom")


app = App()
app.mainloop()
