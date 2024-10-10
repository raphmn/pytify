import ctypes

from app.navigator import *
from app.search_frame import *
from app.results_frame import *
from app.artists_frame import *
from app.album_frame import *


def setup():
    application_id = 'nsi.project.spotify.1_0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(application_id)

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry('1280x720')
        self.title('Pytify')
        self.iconbitmap('media/appicon/appicon_w.ico')
        self.resizable(True, True)

        self.pack_propagate(False)

        self.start_page_image = ctk.CTkImage(Image.open('media/start_page.png'), size=(800, 600))
        self.start_page = ctk.CTkLabel(self, text='', image=self.start_page_image)
        self.start_page.pack(anchor=tk.CENTER, side=tk.RIGHT, expand=True)

        self.navigator = LateralFrame(self, width=180, height=1080)
        self.navigator.pack(anchor=tk.NW, side="left")

        self.search_frame = SearchFrame(self, width=750, height=1080)
        self.results_frame = ResultsFrame(self, width=750, height=1080)

        self.artists_frame = ArtistsFrame(self, width=750, height=1080)

        self.albums_frame = AlbumFrame(self, width=750, height=1080)

        self.navigator.search_button_display.trace('w', self.pack_search)
        self.navigator.artists_button_display.trace('w', self.pack_artists)
        self.navigator.albums_button_display.trace('w', self.pack_albums)

        self.search_frame.search.trace('w', self.results_frame.search_update)
        self.search_frame.search.trace('w', self.search_update)



    def pack_search(self, *args):
        if self.navigator.search_button_display.get():

            self.start_page.pack_forget()
            self.artists_frame.pack_forget()
            self.albums_frame.pack_forget()

            self.search_frame.pack(anchor=tk.N, ipady=25, pady=17, ipadx=150)
            self.results_frame.pack(anchor=tk.S, ipady=250, pady=17, ipadx=150)
        else:

            self.search_frame.pack_forget()
            self.results_frame.pack_forget()

            self.start_page.pack(anchor=tk.CENTER, side=tk.RIGHT, expand=True)

    def search_update(self, *args):
        self.results_frame.search.set(self.search_frame.search.get())

    def pack_artists(self, *args):
        if self.navigator.artists_button_display.get():

            self.start_page.pack_forget()
            self.search_frame.pack_forget()
            self.results_frame.pack_forget()
            self.albums_frame.pack_forget()

            self.artists_frame.pack(anchor=tk.CENTER, ipady=25, pady=17, ipadx=150)
        else:

            self.artists_frame.pack_forget()
            self.start_page.pack(anchor=tk.CENTER, side=tk.RIGHT, expand=True)

    def pack_albums(self, *args):
        if self.navigator.albums_button_display.get():

            self.start_page.pack_forget()
            self.search_frame.pack_forget()
            self.results_frame.pack_forget()
            self.artists_frame.pack_forget()

            self.albums_frame.pack(anchor=tk.CENTER, ipady=25, pady=17, ipadx=150)
        else:

            self.albums_frame.pack_forget()
            self.start_page.pack(anchor=tk.CENTER, side=tk.RIGHT, expand=True)



if __name__ == '__main__':
    setup()
    app = App()
    app.mainloop()
