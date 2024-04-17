import customtkinter as ctk
import tkinter as tk

from PIL import Image

import app.database

class SearchFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search = tk.StringVar()

        self.albumsList = app.database.album_style()
        self.styles = []

        for i in range(0, len(self.albumsList)):

            if self.albumsList[i][1] not in self.styles:
                self.styles.append(self.albumsList[i][1])

        self.search_label = ctk.CTkLabel(self, text='Utilisez cette barre pour rechercher un artiste, un album ou un morceau', font=('Segoe UI', 16))
        self.search_label.pack(anchor=tk.N, side=tk.TOP, pady=25)

        self.search_bar = ctk.CTkEntry(self, placeholder_text="Rechercher", width=760, height=60, corner_radius=8,
                                       font=('Segoe UI', 18), textvariable=self.search)
        self.search_bar.pack(expand=True, anchor=tk.N, side='top')

        self.filter_style = ctk.CTkOptionMenu(self, values=[" Style"] + [value for value in self.styles])
        self.filter_style.pack(side='left', padx=25, pady=25)
