import customtkinter as ctk
import tkinter as tk
import app.database


class ResultsFrame(ctk.CTkScrollableFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search = tk.StringVar()

        self.toDisplay = []
        self.toDisplayDict = {}
        self.LabelDict = {}

        self.no_results = ctk.CTkLabel(self, text='Pas de résultats.', font=('Segoe UI', 12), text_color='grey')
        self.start_text = ctk.CTkLabel(self, text="Les résultats s'afficheront ici", font=('Segoe UI', 12),
                                       text_color='grey')
        self.start_text.pack(anchor=tk.CENTER, pady=150)

    def search_update(self, *args):

        for i in range(len(self.toDisplay)):
            self.toDisplayDict[i].pack_forget()
            self.LabelDict[i].pack_forget()

        self.toDisplay = []
        self.toDisplayDict = {}
        self.LabelDict = {}

        self.start_text.pack_forget()
        self.no_results.pack_forget()

        for i in range(1, len(app.database.Albums)):
            if app.database.Albums[i][0][:len(self.search.get())].lower() == self.search.get().lower():
                self.toDisplay.append(app.database.Albums[i][0])

        for i in range(1, len(app.database.Artistes)):
            if app.database.Artistes[i][0][:len(self.search.get())].lower() == self.search.get().lower():
                self.toDisplay.append(app.database.Artistes[i][0])

        for i in range(0, len(self.toDisplay)):
            self.toDisplayDict[i] = ctk.CTkFrame(self, width=400, height=250, border_color='grey', border_width=1)

            self.LabelDict[i] = ctk.CTkLabel(self.toDisplayDict[i], text=str(self.toDisplay[i]))

            self.toDisplayDict[i].pack(anchor=tk.NW, side=tk.BOTTOM, expand=True, pady=20, padx=20, ipadx=500)
            self.LabelDict[i].pack(anchor=tk.W, pady=20, padx=20)

        print(self.toDisplay)

        if self.toDisplay == []:
            self.no_results.pack(anchor=tk.CENTER, pady=150)
