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

    left_sidebar = ttk.Frame(root, width=150, relief="groove", padding=5)
    left_sidebar.grid(row=1, column=0, rowspan=2, sticky="ns")
    ttk.Button(left_sidebar, text="Item 1").pack(pady=5)
    ttk.Button(left_sidebar, text="Item 2").pack(pady=5)
    ttk.Button(left_sidebar, text="Item 3").pack(pady=5)

    main_content = ttk.Frame(root, relief="groove", padding=5)
    main_content.grid(row=1, column=1, sticky="nsew")
    ttk.Label(main_content, text="Main Content Area", font=("Arial", 16)).pack(pady=20)

    right_sidebar = ttk.Frame(root, width=150, relief="groove", padding=5)
    right_sidebar.grid(row=1, column=2, sticky="ns")
    ttk.Label(right_sidebar, text="details/stats").pack(pady=5)
    ttk.Label(right_sidebar, text="Info 1").pack(pady=5)
    ttk.Label(right_sidebar, text="Info 2").pack(pady=5)

    bottom_bar = ttk.Frame(root, height=50, relief="groove", padding=5)
    bottom_bar.grid(row=2, column=1, sticky="ew")
    ttk.Label(bottom_bar, text="Notification/COntrols").pack(pady=5)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

create_game_layout()
