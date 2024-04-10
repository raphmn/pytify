import customtkinter as ctk
import tkinter as tk

from PIL import Image


class SearchFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search = tk.StringVar()

        self.search_bar = ctk.CTkEntry(self, placeholder_text="Rechercher", width=550, height=60, corner_radius=8,
                                       font=('Segoe UI', 18), textvariable=self.search)
        self.search_bar.pack(expand=True, anchor=tk.CENTER, side=tk.LEFT)

        self.delete_button = ctk.CTkButton(self, text='X', font=('Segoe UI', 18), fg_color='transparent',
                                           text_color='white', command=self.reset_search)
        self.delete_button.pack(side=tk.LEFT, ipadx=20, pady=10)

    def reset_search(self):
        self.search.set("")
