import customtkinter as ctk
import tkinter as tk

from PIL import Image
import ctypes

from app.player_frame import *
from app.navigator import *
from app.search import *

def setup():
    application_id = 'nsi.project.spotify.1_0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(application_id)

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x720')
        self.title('Pytify')
        self.iconbitmap('media/appicon/appicon_w.ico')

        self.navigator = LateralFrame(self, width=180, height=1080)
        self.navigator.pack(anchor=tk.NW, side="left")

        self.search_frame = SearchFrame(self, width=1050, height=170)
        self.search_frame.pack(anchor=tk.N, pady=30)


if __name__ == '__main__':
    setup()
    app = App()
    app.mainloop()
