import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

current_pressed_enemy = None
player_skill = 1
player_damage = player_skill
current_pressed_sidebar_button = None
auto_attack_id = None

def highlight_enemy(event):
    global current_pressed_enemy, health_bar, health_label, bottom_bar, enemy_healths, max_health
    
    health_bar.place_forget()
    health_label.place_forget()

    if current_pressed_enemy:
        current_pressed_enemy.config(highlightbackground="white", highlightthickness=1)
    
    current_pressed_enemy = event.widget
    current_pressed_enemy.config(highlightbackground="red", highlightthickness=2)

    enemy_health = enemy_healths.get(current_pressed_enemy)
    if enemy_health:
        health_bar_width = bottom_bar.winfo_width()  
        health_bar.place(x=0, y=0, width=health_bar_width, height=bottom_bar.winfo_height())
        health_label.config(text=str(enemy_health))
        health_label.place(relx=0.5, rely=0.5, anchor='center')
        

def sidebar_button_click(event):
    global current_pressed_sidebar_button

    if current_pressed_sidebar_button:
        current_pressed_sidebar_button.config(background="SystemButtonFace")
    
    button = event.widget
    button.config(background="green")

    current_pressed_sidebar_button = button

def update_skill_value():
    print(f"Updating skill to: {player_skill}")
    skill_buttons[0].config(text=f"Attack ({player_skill})")

def attack_enemy():
    global current_pressed_enemy, enemy_healths, player_skill, player_damage
    if current_pressed_enemy is None:
        print("No enemy selected!")
        return
    
    enemy_health = enemy_healths.get(current_pressed_enemy)
    if enemy_health is None:
        print("Selected enemy does not have recorded health!")
        return

    enemy_health -= player_damage
    if enemy_health <= 0:
        enemy_health = 0
        enemy_index = list(enemy_healths).index(current_pressed_enemy) + 1
        skill_increase = max(enemy_index, round(0.01 * enemy_healths[current_pressed_enemy]))
        player_skill += skill_increase
        print(f"New player skill after defeating enemy: {player_skill}")
        player_damage = player_skill * 1
        update_skill_value()
        current_pressed_enemy.unbind("<Button-1>")
    else:
        enemy_healths[current_pressed_enemy] = enemy_health
    
    update_enemy_health_display(enemy_health)

def update_enemy_health_display(enemy_health):
    health_bar_width = bottom_bar.winfo_width()
    health_bar.place(x=0, y=0, width=health_bar_width, height=bottom_bar.winfo_height())
    health_label.config(text=str(enemy_health))
    health_label.place(relx=0.5, rely=0.5, anchor='center')

def auto_attack():
    global auto_attack_id
    attack_enemy()  
    auto_attack_id = root.after(1000, auto_attack)  

def start_auto_attack():
    global auto_attack_id
    if auto_attack_id is None:
        auto_attack()  

def stop_auto_attack():
    global auto_attack_id
    if auto_attack_id is not None:
        root.after_cancel(auto_attack_id)
        auto_attack_id = None

def create_game_layout_with_progression():
    root =tk.Tk()
    root.title("Game Layout")
    root.geometry("1050x800")

    global bottom_bar, health_bar, health_label, enemy_healths, max_health, current_pressed_sidebar_button  
    global player_skill, player_damage
    
    player_skill = 1
    player_damage = player_skill

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (1000 / 2)
    y_coordinate = (screen_height / 2) - (1000 / 2)

    root.geometry(f"+{int(x_coordinate)}+{int(y_coordinate)}")

    bottom_bar = ttk.Frame(root, height=50, relief="groove", padding=5)
    bottom_bar.grid(row=2, column=1, sticky="ew")
    ttk.Button(bottom_bar, text="Auto Attack", command=start_auto_attack).pack(side="left", padx=20)
    ttk.Button(bottom_bar, text="Stop Auto Attack", command=stop_auto_attack).pack(side="left", padx=20)
    ttk.Label(bottom_bar, text="Notification/Controls").pack(pady=5)

    style = ttk.Style()
    style.configure('TFrame', background='#FCE6C9')
    style.configure('TButton', background='#FCE6C9', foreground='black')

    left_sidebar = ttk.Frame(root, width=150, relief="groove", padding=5)
    left_sidebar.grid(row=1, column=0, rowspan=2, sticky="ns")

    skill_names = ["attack"]
    skill_values = [player_skill]

    def reset_enemy_healths():
        global enemy_healths, current_pressed_enemy, health_bar, health_label, bottom_bar

        enemy_healths_value = 250
        for canvas in enemy_healths:
            enemy_healths[canvas] = round(enemy_healths_value)
            enemy_healths_value *= 2.5
            canvas.bind("<Button-1>", highlight_enemy)
        
        if current_pressed_enemy:
            enemy_health = enemy_healths.get(current_pressed_enemy)
        if enemy_health:
            health_bar_width = bottom_bar.winfo_width()  
            health_bar.place(x=0, y=0, width=health_bar_width, height=bottom_bar.winfo_height())
            health_label.config(text=str(enemy_health))
            health_label.place(relx=0.5, rely=0.5, anchor='center')

    reset_button = tk.Button(root, text="RESET", bg="orange", command=reset_enemy_healths, font=("Arial", 16), padx=-9, anchor="e")
    reset_button.place(relx=1.0, rely=1.0, anchor="se", x=0, y=0)

    attack_button = tk.Button(root, text="Attack", bg="red", command=attack_enemy, font=("Arial", 16))
    attack_button.place(relx=0.01, rely=0.01, anchor="nw")

    skill_buttons = []
    for i, (skill_name, skill_value) in enumerate(zip(skill_names, skill_values)):
        button_text = f"{skill_name} ({skill_value})"
        button = tk.Button(left_sidebar, text=button_text, width=25)
        button.pack(pady=5)
        button.bind("<Button-1>", sidebar_button_click)
        skill_buttons.append(button)




    def highlight_enemy(event):
        global current_pressed_enemy, health_bar, health_label, bottom_bar, enemy_healths, max_health
        global player_skill, player_damage

        health_bar.place_forget()
        health_label.place_forget()

        if current_pressed_enemy:
            current_pressed_enemy.config(highlightbackground="white", highlightthickness=1)

        current_pressed_enemy = event.widget
        current_pressed_enemy.config(highlightbackground="red", highlightthickness=2)

        enemy_health = enemy_healths.get(current_pressed_enemy)
        if enemy_health:
            enemy_health -= player_damage
            if enemy_health <= 0:
                enemy_health = 0
                enemy_index = list(enemy_healths).index(current_pressed_enemy) + 1
                skill_increase = max(enemy_index, round(0.01 * enemy_healths[current_pressed_enemy]))  
                player_skill += skill_increase
                print(f"New player skill after defeating enemy: {player_skill}")  
                player_damage = player_skill * 1
                update_skill_value()
                current_pressed_enemy.unbind("<Button-1>")
            else:
                enemy_healths[current_pressed_enemy] = enemy_health

            health_bar_width = bottom_bar.winfo_width()  
            health_bar.place(x=0, y=0, width=health_bar_width, height=bottom_bar.winfo_height())
            health_label.config(text=str(enemy_health))
            health_label.place(relx=0.5, rely=0.5, anchor='center')

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

    health_bar = tk.Canvas(bottom_bar, bg="red", bd=0, highlightthickness=0)
    health_label = ttk.Label(bottom_bar, font=("Arial", 14), background="red", foreground="white")

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
        "pictures/enemy11.jpg",
        "pictures/enemy12.jpg",
        "pictures/enemy13.jpg",
        "pictures/enemy14.jpg",
        "pictures/enemy15.jpg",
    ]

    cm_to_pixel = 37.8
    size = (int(3.5 * cm_to_pixel), int(4 * cm_to_pixel))

    enemy_images = [ImageTk.PhotoImage(Image.open(image_path).resize(size)) for image_path in enemy_image_paths]

    enemy_healths = {}
    enemy_healths_value = 250
    for i, enemy_image in enumerate(enemy_images):
        canvas = tk.Canvas(main_content, width=size[0], height=size[1], bd=0, highlightthickness=1)
        canvas.create_image(size[0]//2, size[1]//2, image=enemy_image)
        canvas.grid(row=(i // 5) + 1, column=i % 5, padx=10, pady=10)
        canvas.bind("<Button-1>", highlight_enemy)

        enemy_healths[canvas] = round(enemy_healths_value)
        enemy_healths_value *= 2.5

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

create_game_layout_with_progression()
