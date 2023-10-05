import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

current_pressed_enemy = None

def highlight_enemy(event):
    global current_pressed_enemy
    
    if current_pressed_enemy:
        current_pressed_enemy.config(relief="raised", borderwidth=1)

    current_pressed_enemy = event.widget
    current_pressed_enemy.config(relief="sunken", borderwidth=3)

def create_game_layout():
    root =tk.Tk()
    root.title("Game Layout")
    root.geometry("1000x800")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (1000 / 2)
    y_coordinate = (screen_height / 2) - (1000 / 2)

    root.geometry(f"+{int(x_coordinate)}+{int(y_coordinate)}")

    top_menu = ttk.Frame(root, height=50, relief="groove", padding=5)
    top_menu.grid(row=0, column=0, columnspan=3, sticky="ew")
    ttk.Button(top_menu, text="Menu 1"). pack(side="left", padx=5)
    ttk.Button(top_menu, text="Menu 2"). pack(side="left", padx=5)
    ttk.Button(top_menu, text="Menu 3"). pack(side="left", padx=5)

    left_sidebar = ttk.Frame(root, width=150, relief="groove", padding=5)
    left_sidebar.grid(row=1, column=0, rowspan=2, sticky="ns")
    for i in range(1, 9):
        ttk.Button(left_sidebar, text=f"Item {i}").pack(pady=5)

    main_content = tk.Frame(root, relief="groove", bg="white")
    main_content.grid(row=1, column=1, sticky="nsew")
    ttk.Label(main_content, text="Main Content Area", font=("Arial", 16)).grid(row=0, column=0, columnspan=5, pady=20)

    right_sidebar = ttk.Frame(root, width=150, relief="groove", padding=5)
    right_sidebar.grid(row=1, column=2, sticky="ns")
    ttk.Label(right_sidebar, text="details/stats").pack(pady=5)
    ttk.Label(right_sidebar, text="Info 1").pack(pady=5)
    ttk.Label(right_sidebar, text="Info 2").pack(pady=5)

    bottom_bar = ttk.Frame(root, height=50, relief="groove", padding=5)
    bottom_bar.grid(row=2, column=1, sticky="ew")
    ttk.Label(bottom_bar, text="Notification/Controls").pack(pady=5)

    enemy_image_paths = [
        "pictures/enemy1.jpg",
        "pictures/enemy2.jpg",
        "pictures/enemy3.jpg",
        "pictures/enemy4.jpg",
        "pictures/enemy5.jpg",
        "pictures/enemy6.jpg",
        "pictures/enemy7.jpg",
        "pictures/enemy8.jpg",
        "pictures/enemy9.jpg",
        "pictures/enemy10.jpg",
    ]

    cm_to_pixel = 37.8
    size = (int(3.5 * cm_to_pixel), int(4 * cm_to_pixel))

    enemy_images = [ImageTk.PhotoImage(Image.open(image_path).resize(size)) for image_path in enemy_image_paths]

    for i, enemy_image in enumerate(enemy_images):
        enemy_btn = ttk.Button(main_content, image=enemy_image)
        enemy_btn.grid(row=(i // 5) + 1, column=i % 5, padx=10, pady=10)
        enemy_btn.bind("<Button-1>", highlight_enemy)
    
    for i, enemy_image in enumerate(enemy_images):
        enemy_btn = tk.Button(main_content, image=enemy_image)
        enemy_btn.grid(row=(i // 5) + 1, column=i % 5, padx=10, pady=10)
        enemy_btn.bind("<Button-1>", highlight_enemy)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

create_game_layout()
