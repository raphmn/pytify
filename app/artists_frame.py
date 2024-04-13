import customtkinter as ctk
import tkinter as tk

from PIL import Image

import app.database


class ArtistsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        self.framesLabels = {}
        self.frames = {}
        self.playButtons = {}

        for i in range(1, len(app.database.Artistes)):

            self.frames[i] = ctk.CTkFrame(self, width=200, height=250)
            self.framesLabels[i] = ctk.CTkLabel(self.frames[i], text=str(app.database.Artistes[i][0]))

            self.frames[i].pack(anchor=tk.NW, side=tk.LEFT, padx=20, pady=20, ipadx=20, ipady=20)
            self.framesLabels[i].pack(anchor=tk.N, pady=25)

            self.playButtons[i] = ctk.CTkButton(self.frames[i], text='►', width=30, height=30, fg_color='transparent', border_color='blue')
            self.playButtons[i].pack(anchor=tk.SE, expand=True, padx=15, pady=15)
