import customtkinter as ctk
import tkinter as tk

from app.artists_details_frame import *
import app.database


class ArtistsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.artist_detailed_frame = None
        self.framesLabels = {}
        self.frames = {}
        self.playButtons = {}

        self.packFrames = {}
        self.frameIndex = 1
        
        artist_search_button = ctk.CTkButton(self, text="Rechercher un artiste a partir d'un morceau", command=lambda artiste1=['Travis Scott']: app.database.artiste_from_song(artiste1))
        artist_search_button.pack(anchor=tk.S, pady=20, padx=20)

        for k in range(1, (len(app.database.Artistes) // 5)+2):
            self.packFrames[k] = ctk.CTkFrame(self, width=750, height=275)
            self.packFrames[k].pack(anchor=tk.NW, pady=20, padx=20, expand=False)

        for i in range(1, len(app.database.Artistes)+1):

            if len(self.packFrames[self.frameIndex].winfo_children()) == 5:
                self.frameIndex += 1

            self.frames[i] = ctk.CTkFrame(self.packFrames[self.frameIndex], width=200, height=250, border_color='grey',
                                          border_width=1)
            self.framesLabels[i] = ctk.CTkLabel(self.frames[i], text=str(app.database.Artistes[i][0]))

            print("added " + str(app.database.Artistes[i][0]))

            self.frames[i].pack(anchor=tk.NW, side=tk.LEFT, padx=20, pady=20, ipadx=50, ipady=20, expand=False)
            self.framesLabels[i].pack(anchor=tk.N, pady=25)

            self.playButtons[i] = ctk.CTkButton(self.frames[i], text='►', width=30, height=30, fg_color='transparent',
                                                border_color='blue', command=lambda i=i: self.show_artist_details(i))
            print('added button with artist id ' + str(i))
            self.playButtons[i].pack(anchor=tk.SE, expand=True, padx=15, pady=15)

    def show_artist_details(self, artist_id):

        self.artist_detailed_frame = ArtistDetailsFrame(self, artist_id=artist_id)
        self.artist_detailed_frame.pack()

    