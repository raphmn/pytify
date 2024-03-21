import customtkinter as ctk
import tkinter as tk

from PIL import Image
import ctypes

from player_frame import *

applicationID = 'nsi.project.spotify.1_0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(applicationID)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x500')
        self.title('Spotify')
        self.iconbitmap('media/appicon/appicon.ico')


        self.lateralBar = ctk.CTkFrame(self, width=180, height=500)
        self.lateralBar.pack_propagate(0)
        self.lateralBar.pack(anchor=tk.NW, side="left")

        self.spotify_label = ctk.CTkLabel(self.lateralBar, text='Spotify')
        self.spotify_label.pack(expand=True)

        self.albums_image = ctk.CTkImage(Image.open('media/icons/albums_32.png'))
        self.albums_button = ctk.CTkButton(self.lateralBar, text='Albums', command=self.show_albums,
                                           image=self.albums_image)
        self.albums_button.pack(ipadx=0, ipady=20, expand=True)

        self.artists_image = ctk.CTkImage(Image.open('media/icons/artists_32.png'))
        self.artists_button = ctk.CTkButton(self.lateralBar, text='Artists', command=self.show_artists,
                                            image=self.artists_image)
        self.artists_button.pack(ipadx=0, ipady=20, expand=True)

        self.search_image = ctk.CTkImage(Image.open('media/icons/search_32.png'))
        self.search_button = ctk.CTkButton(self.lateralBar, text='Search', command=self.search_button,image=self.search_image)
        self.search_button.pack(ipadx=0, ipady=20, expand=True)

        self.player_bar = PlayerFrame(self, width=820, height=50)
        self.player_bar.pack(anchor="s", side="bottom")


    def search_button(self):
        print('Search')
        #### A completer

    def show_artists(self):
        print('Artists')
        ### A completer

    def show_albums(self):
        print('Albums')
        #### A completer


app = App()
app.mainloop()