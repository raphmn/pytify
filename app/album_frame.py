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

        self.packFrames = {}
        self.frameIndex = 1


        for i in range(0, len(self.albumsList)):

            if self.albumsList[i][1] not in self.styles:
                self.styles.append(self.albumsList[i][1])

        for k in range(0, len(self.styles)):

            self.stylesFrames[k] = ctk.CTkFrame(self, width=750, height=250, border_color='grey', border_width=1)
            self.stylesLabels[k] = ctk.CTkLabel(self.stylesFrames[k], text=str(self.styles[k]), font=('Segoe UI', 20))

            self.stylesFrames[k].pack(anchor=tk.NW, pady=10, padx=10, ipadx=500, expand=True)
            self.stylesLabels[k].pack(anchor=tk.NW, pady=10, padx=10)

            for n in range(1, (len(app.database.Albums) // 5) + 2):
                self.packFrames[n] = ctk.CTkFrame(self.stylesFrames[k], width=750, height=250)
                self.packFrames[n].pack(anchor=tk.NW, pady=20, padx=20, expand=False)

            for j in range(0, len(self.albumsList)):

                if len(self.packFrames[self.frameIndex].winfo_children()) == 8:
                    self.frameIndex += 1

                if self.albumsList[j][1] == self.styles[k]:
                    self.albumFrames[j] = ctk.CTkFrame(self.packFrames[self.frameIndex], width=200, height=250)
                    self.albumLabels[j] = ctk.CTkLabel(self.albumFrames[j], text=str(self.albumsList[j][0]))

                    self.albumFrames[j].pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10, expand=False)
                    self.albumLabels[j].pack(anchor=tk.N, pady=10, padx=10)

            for h in range(1, len(self.packFrames)+1):
                if self.packFrames[h].winfo_children() == []:
                    self.packFrames[h].destroy()

        self.add_album = ctk.CTkButton(self, text='+ Ajouter un album', command=app.database.add_album, width=150, height=60)
        self.delete_album = ctk.CTkButton(self, text='- Supprimer un album', command=app.database.delete_album, width=150, height=60)

        self.add_album.pack(anchor=tk.CENTER, side='left', padx=20, pady=20)
        self.delete_album.pack(anchor=tk.CENTER, side='left', padx=20, pady=20)
        