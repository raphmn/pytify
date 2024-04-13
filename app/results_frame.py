import customtkinter as ctk
import tkinter as tk
import app.database

from PIL import Image


class ResultsFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        self.search = tk.StringVar()

        self.toDisplay = []
        self.toDisplayDict = {}
        self.LabelDict = {}

    def search_update(self, *args):

        for i in range(len(self.toDisplay)):
            self.toDisplayDict[i].pack_forget()
            self.LabelDict[i].pack_forget()

        self.toDisplay = []
        self.toDisplayDict = {}
        self.LabelDict = {}

        for i in range(1, len(app.database.Albums)):
            if app.database.Albums[i][0][:len(self.search.get())].lower() == self.search.get().lower():
                self.toDisplay.append(app.database.Albums[i][0])

        for i in range(1, len(app.database.Artistes)):
            if app.database.Artistes[i][0][:len(self.search.get())].lower() == self.search.get().lower():
                self.toDisplay.append(app.database.Artistes[i][0])

        for i in range(len(self.toDisplay)):
            self.toDisplayDict[i] = ctk.CTkFrame(self, width=200, height=250)

            self.LabelDict[i] = ctk.CTkLabel(self.toDisplayDict[i], text=str(self.toDisplay[i]))

            self.toDisplayDict[i].pack(anchor=tk.NW, side=tk.LEFT, expand=True, ipady=20, ipadx=20, pady=20, padx=20)
            self.LabelDict[i].pack(anchor=tk.CENTER, ipady=20, ipadx=20, pady=20, padx=20)
