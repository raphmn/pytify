import customtkinter as ctk
import tkinter as tk

from PIL import Image

import app.database


class ArtistDetailsFrame(ctk.CTkFrame):

    def __init__(self, master, artist_id, **kwargs):
        super().__init__(master, artist_id, **kwargs)

        self.artist = app.database.Artistes[artist_id]
        print(artist_id)
        print(self.artist)
        self.artist_image = ctk.CTkImage(Image.open("media/icons/placeholder.png"), size=(128, 128))

        self.artist_label = ctk.CTkLabel(self, text=str(self.artist[0]), font=('Segoe UI', 24), image=self.artist_image)
        self.artist_info = ctk.CTkLabel(self, text="Nom: " + str(self.artist[1]) + ", Âge: " + str(
            self.artist[3]) + "ans (" + str(self.artist[2]) + "), Origine: " + str(self.artist[4]))

        self.artist_label.pack(anchor=tk.NW, padx=150, pady=150, side='top')
        self.artist_info.pack(side='left', pady=10)

        self.albums_label = ctk.CTkLabel(self, text='Albums', font=('Segoe UI', 16))
        self.albums_label.pack(side='top')

        self.artist_albums = app.database.album_from_artist(self.artist[0])
        print(self.artist_albums)

        self.albums_frame_dict = {}
        self.albums_label_dict = {}
        self.albums_image_dict = {}

        self.albums_list_frame = ctk.CTkFrame(self, width=750, height=250)
        self.albums_list_frame.pack(side='top', pady=10, ipadx=500)

        for i in range(0, len(self.artist_albums)):
            self.albums_frame_dict[i] = ctk.CTkFrame(self.albums_list_frame, width=250, height=250)
            self.albums_image_dict[i] = ctk.CTkImage(Image.open('media/icons/placeholder.png'), size=(64,64))
            self.albums_label_dict[i] = ctk.CTkLabel(self.albums_frame_dict[i], text=self.artist_albums[i][1], image=self.albums_image_dict[i])

            self.albums_frame_dict[i].pack(expand=False, padx=10, pady=10, side='left')
            self.albums_label_dict[i].pack(side='top', pady=1)


