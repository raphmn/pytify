import customtkinter as ctk
import tkinter as tk

from PIL import Image


class LateralFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        self.spotify_image_frame = ctk.CTkFrame(self, width=128, height=128)
        self.spotify_image_frame.pack(expand=True)

        self.spotify_label = ctk.CTkLabel(self, text='pytify')
        self.spotify_label.pack(expand=True)

        self.albums_image = ctk.CTkImage(Image.open('media/icons/albums_32.png'))
        self.albums_button = ctk.CTkButton(self, text='Albums',
                                           image=self.albums_image)
        self.albums_button.pack(ipadx=0, ipady=20, expand=True)

        self.artists_image = ctk.CTkImage(Image.open('media/icons/artists_32.png'))
        self.artists_button = ctk.CTkButton(self, text='Artists',
                                            image=self.artists_image, command=self.change_artist_display)
        self.artists_button.pack(ipadx=0, ipady=20, expand=True)

        self.search_image = ctk.CTkImage(Image.open('media/icons/search_32.png'))
        self.search_button = ctk.CTkButton(self, text='Search',
                                           image=self.search_image, command=self.change_search_display)
        self.search_button.pack(ipadx=0, ipady=20, expand=True)

        self.search_button_display = tk.BooleanVar()
        self.albums_button_display = tk.BooleanVar()
        self.artists_button_display = tk.BooleanVar()

    def change_search_display(self):
        self.search_button_display.set((True if not self.search_button_display.get() else False))

    def change_album_display(self):
        self.albums_button_display.set((True if not self.albums_button_display.get() else False))

    def change_artist_display(self):
        self.artists_button_display.set((True if not self.artists_button_display.get() else False))




