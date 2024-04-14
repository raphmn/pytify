import customtkinter as ctk
import tkinter as tk

import app.database


class AlbumFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.albumsList = app.database.album_style()
        self.styles = []

        self.stylesFrames = {}
        self.stylesLabels = {}

        self.albumFrames = {}
        self.albumLabels = {}

        for i in range(0, len(self.albumsList)):

            if self.albumsList[i][1] not in self.styles:
                self.styles.append(self.albumsList[i][1])

        for k in range(0, len(self.styles)):

            self.stylesFrames[k] = ctk.CTkFrame(self, width=750, height=250, border_color='grey', border_width=1)
            self.stylesLabels[k] = ctk.CTkLabel(self.stylesFrames[k], text=str(self.styles[k]), font=('Segoe UI', 20))

            self.stylesFrames[k].pack(anchor=tk.NW, pady=10, padx=10, ipadx=500, expand=True)
            self.stylesLabels[k].pack(anchor=tk.NW, pady=10, padx=10)

            for j in range(0, len(self.albumsList)):
                if self.albumsList[j][1] == self.styles[k]:
                    self.albumFrames[j] = ctk.CTkFrame(self.stylesFrames[k], width=200, height=250)
                    self.albumLabels[j] = ctk.CTkLabel(self.albumFrames[j], text=str(self.albumsList[j][0]))

                    self.albumFrames[j].pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10, expand=False)
                    self.albumLabels[j].pack(anchor=tk.N, pady=10, padx=10)
