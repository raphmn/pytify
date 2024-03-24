import customtkinter as ctk
import tkinter as tk

from PIL import Image


class LateralFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(0)

        self.spotify_image_frame = ctk.CTkFrame(self, width=128, height=128)
        self.spotify_image_frame.pack(expand=True)

        self.spotify_label = ctk.CTkLabel(self, text='Spotify')
        self.spotify_label.pack(expand=True)

        self.albums_image = ctk.CTkImage(Image.open('media/icons/albums_32.png'))
        self.albums_button = ctk.CTkButton(self, text='Albums',
                                           image=self.albums_image)
        self.albums_button.pack(ipadx=0, ipady=20, expand=True)

        self.artists_image = ctk.CTkImage(Image.open('media/icons/artists_32.png'))
        self.artists_button = ctk.CTkButton(self, text='Artists',
                                            image=self.artists_image)
        self.artists_button.pack(ipadx=0, ipady=20, expand=True)

        self.search_image = ctk.CTkImage(Image.open('media/icons/search_32.png'))
        self.search_button = ctk.CTkButton(self, text='Search',
                                           image=self.search_image)
        self.search_button.pack(ipadx=0, ipady=20, expand=True)

