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

        self.start_page_image = ctk.CTkImage(Image.open('media/start_page.png'), size=(800, 600))
        self.start_page = ctk.CTkLabel(self, text='', image=self.start_page_image)
        self.start_page.pack(anchor=tk.CENTER, side=tk.RIGHT, expand=True)

        self.navigator = LateralFrame(self, width=180, height=1080)
        self.navigator.pack(anchor=tk.NW, side="left")

        self.search_frame = SearchFrame(self, width=1050, height=170)

        self.navigator.search_button_state.trace('w', self.pack_search)

    def pack_search(self, *args):
        self.start_page.destroy()
        self.search_frame.pack(anchor=tk.N, pady=30)


if __name__ == '__main__':
    setup()
    app = App()
    app.mainloop()
