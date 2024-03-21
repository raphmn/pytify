import customtkinter as ctk
import tkinter as tk


class Player(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.player_frame = ctk.CTkFrame(self, height=100, width=1000)
        self.player_frame.pack()

        self.next_image = tk.PhotoImage(file='media/next.png')
        self.next_button = ctk.CTkButton(self, text='Next', image=self.next_image)
        self.next_button.pack()

        self.previous_image = tk.PhotoImage(file='media/previous.png')
        self.previous_button = ctk.CTkButton(self, text='Previous', image=self.previous_image)
        self.previous_button.pack()

        self.pause_image = tk.PhotoImage(file='media/play.png')
        self.pause_button = ctk.CTkButton(self, text='Pause', image=self.pause_image)
        self.pause_button.pack()
