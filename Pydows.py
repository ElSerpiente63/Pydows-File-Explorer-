import tkinter as tk
from tkinter import Tk
from tkinter import ttk
import os
from tkinter import Canvas
from PIL import ImageTk
from PIL import Image 
#Idées 
  #-option ouvrir vscode avec le projet mf app d'ouvert 
class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Pydows File Explorer')
        self.frm = ttk.Frame(self)
        self.frm.pack()
        self.text_frame = tk.LabelFrame(text="Pydows")
        self.text_frame.pack()
        self.search = tk.Entry(self.frm, width=100)
        self.search.pack(side='left', padx=(10,10))
        self._button_ = ttk.Button(self.frm, text="search", command=self.list_dir)
        self._button_.pack(side='left', padx=(10,0))
        self.other_frame = ttk.Frame(self)
        self.other_frame.pack(padx=20, pady=20)
        self.scrollbar = tk.Scrollbar(self.other_frame)
        self.scrollbar.pack(side="right", fill="both")
        self.second_frame = ttk.Frame(self)
        self.second_frame.pack(side="left")
        self.second_frame.place(x=0, y=20)
        self.style = ttk.Style()
        self.style.configure("ColoredSeparator.TSeparator", background="light gray")
        self.first_separator = ttk.Separator(self, orient="vertical", style='ColoredSeparator.TSeparator')
        self.first_separator.pack(fill="y", padx=10, pady=0)
        liste_acces_rapide = ["Bureau", "Documents", "Téléchargements", "Images", "AT-PGN", "config", "simplepost.ino"]
        for i in range(7):
            self.___button___ = ttk.Button(self.second_frame, text=str(liste_acces_rapide[i]), width=15)
            self.___button___.place(x=0, y=i)
            self.___button___.pack()
        print(self["bg"])
        self.mainloop()
        
    def add_button(self):
        self.button_ = ttk.Button(text="Button Added", command=print('nothing')).grid(column=0, row=0)

    def list_dir(self):
        os.chdir("C:/")
        liste_dir = os.listdir()
        for i in range(len(liste_dir)):
            self.__button__ = ttk.Button(self.other_frame,text=f"{liste_dir[i]}", command=print(i), width=150)
            self.__button__.pack(side="top", padx=(0,0))
        print(f'Il y a {len(liste_dir)} fichier et dossiers')
    def delete_file(self, file):
        # input avant box dialog (test)
        inputing = input(f"Voulez vous vraiment supprimer{file} ?")
#sorte de recycle view valables pour tout les path
class PageSearch(tk.Frame):
    def __init__(self, path: str):
        self.searchbar = tk.Entry(self, width=100)
        self.search_button = ttk.Button(self, text="search", command=self.search)
        self.search_button.pack()
        os.chdir(path)
        self.contain = os.listdir(path)
        self._frame_ = ttk.Frame(self)
        self._frame_.place(x=0, y=20)
        for i in range(len(self.contain)):
            self.____button____ = ttk.Button(self, text=f"{self.contain[i]}")
            self.____button____.pack(width=100)
        

MainWindow()