import customtkinter as ctk
import tkinter as tk

from PIL import Image


class PlayerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.previous_image = ctk.CTkImage(Image.open('media/control/previous.png'))
        self.previous_button = ctk.CTkButton(master=self, text='', image=self.previous_image, fg_color='transparent')
        self.previous_button.pack(anchor=tk.S, expand=True, side="left")

        self.pause_image = ctk.CTkImage(Image.open('media/control/play.png'))
        self.pause_button = ctk.CTkButton(master=self, text='', image=self.pause_image, fg_color='transparent')
        self.pause_button.pack(anchor=tk.S, expand=True, side="left")

        self.next_image = ctk.CTkImage(Image.open('media/control/next.png'))
        self.next_button = ctk.CTkButton(master=self, text='', image=self.next_image, fg_color='transparent')
        self.next_button.pack(anchor=tk.S, expand=True, side="left")

