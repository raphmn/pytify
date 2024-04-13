import customtkinter as ctk
import tkinter as tk

from PIL import Image

import app.database


class AlbumFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        self.albumsList = app.database.album_style()
        self.styles = []

        self.stylesFrames = {}
        self.stylesLabels = {}

        for i in range(1, len(self.albumsList)):

            if self.albumsList[i][1] not in self.styles:
                self.styles.append(self.albumsList[i][1])

        for i in range(1, len(self.styles)):

            self.stylesFrames[i] = ctk.CTkFrame(self, width=750, height=250)
            self.stylesLabels[i] = ctk.CTkLabel(self.stylesFrames[i], text=str(self.styles[i]), font=('Segoe UI', 14))

            self.stylesFrames[i].pack(anchor=tk.NW, pady=10,padx=10)
            self.stylesLabels[i].pack(anchor=tk.NW, pady=10, padx=10)






