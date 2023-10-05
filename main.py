import tkinter as tk
from tkinter import ttk

def create_game_layout():
    root =tk.Tk()
    root.title("Game Layout")
    root.geometry("800x600")

    top_menu = ttk.Frame(root, height=50, relief="groove", padding=5)
    top_menu.grid(row=0, column=0, columnspan=3, sticky="ew")
    ttk.Button(top_menu, text="Menu 1"). pack(side="left", padx=5)
    ttk.Button(top_menu, text="Menu 2"). pack(side="left", padx=5)
    ttk.Button(top_menu, text="Menu 3"). pack(side="left", padx=5)


    root.mainloop()
