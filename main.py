import tkinter as tk
from formations import formations

def change_formation(*args):
    update_player_positions()

def update_squad_name(event=None):
    name = squad_entry.get()

    if name.strip() == "":
        squad_heading.config(text="My Squad")
    else:
        squad_heading.config(text=name)

root = tk.Tk()

root.title("Football Lineup Builder")
root.geometry("900x700")

controls = tk.Frame(root)
controls.pack(pady=10)

squad_label = tk.Label(
    controls,
    text="Squad Name:"
)

squad_label.pack(side="left", padx=5)

squad_entry = tk.Entry(
    controls,
    width=20
)

squad_entry.bind("<Return>", update_squad_name)

squad_entry.pack(side="left", padx=5)

squad_heading = tk.Label(
    root,
    text="My Squad",
    font=("Arial", 18, "bold")
)

squad_heading.pack()

formation_label = tk.Label(
    controls,
    text="Formation:"
)

formation_label.pack(side="left", padx=5)

formation_var = tk.StringVar()

formation_var.set("4-3-3")

formation_var.trace_add("write", change_formation)

formation_menu = tk.OptionMenu(
    controls,
    formation_var,
    "4-3-3",
    "4-4-2",
    "4-2-3-1"
)

formation_menu.pack(side="left", padx=5)

pitch = tk.Canvas(
    root,
    width=700,
    height=600,
    bg="green"
)

pitch.pack(pady=10)

# Outer boundary
pitch.create_rectangle(
    20, 20,
    680, 580,
    outline="white",
    width=3
)

# Halfway line
pitch.create_line(
    20, 300,
    680, 300,
    fill="white",
    width=3
)

# Centre circle
pitch.create_oval(
    300, 250,
    400, 350,
    outline="white",
    width=3
)

# Centre spot
pitch.create_oval(
    346, 296,
    354, 304,
    fill="white",
    outline="white"
)

# Top penalty area
pitch.create_rectangle(
    220, 20,
    480, 120,
    outline="white",
    width=3
)

# Top goal
pitch.create_rectangle(
    300, 5,
    400, 20,
    outline="white",
    width=3
)

# Bottom penalty area
pitch.create_rectangle(
    220, 480,
    480, 580,
    outline="white",
    width=3
)

# Bottom goal
pitch.create_rectangle(
    300, 580,
    400, 595,
    outline="white",
    width=3
)

players = [
    {"name": "Player 1", "number": 1, "position": "GK"},
    {"name": "Player 2", "number": 2, "position": "RB"},
    {"name": "Player 3", "number": 3, "position": "CB"},
    {"name": "Player 4", "number": 4, "position": "CB"},
    {"name": "Player 5", "number": 5, "position": "LB"},
    {"name": "Player 6", "number": 6, "position": "CM"},
    {"name": "Player 7", "number": 7, "position": "CM"},
    {"name": "Player 8", "number": 8, "position": "CM"},
    {"name": "Player 9", "number": 9, "position": "RW"},
    {"name": "Player 10", "number": 10, "position": "ST"},
    {"name": "Player 11", "number": 11, "position": "LW"}
]

positions = formations["4-3-3"]

for i in range(len(players)):
    x, y = positions[i]

    circle_id = pitch.create_oval(
        x - 25,
        y - 25,
        x + 25,
        y + 25,
        fill="white"
    )

    text_id = pitch.create_text(
        x,
        y,
        text=f"{players[i]['number']}\n{players[i]['name']}"
    )

    players[i]["circle_id"] = circle_id
    players[i]["text_id"] = text_id
    players[i]["slot"] = i

    pitch.tag_bind(
    circle_id,
    "<Double-Button-1>",
    lambda event, p=players[i]: edit_player(p)
    )

    pitch.tag_bind(
        text_id,
        "<Double-Button-1>",
        lambda event, p=players[i]: edit_player(p)
    )

    pitch.tag_bind(
        circle_id,
        "<Button-1>",
        lambda event, p=players[i]: start_drag(event, p)
    )

    pitch.tag_bind(
        circle_id,
        "<B1-Motion>",
        lambda event, p=players[i]: drag_player(event, p)
    )

    pitch.tag_bind(
        circle_id,
        "<ButtonRelease-1>",
        lambda event, p=players[i]: stop_drag(event, p)
    )

    pitch.tag_bind(
        text_id,
        "<Button-1>",
        lambda event, p=players[i]: start_drag(event, p)
    )

    pitch.tag_bind(
        text_id,
        "<B1-Motion>",
        lambda event, p=players[i]: drag_player(event, p)
    )

    pitch.tag_bind(
        text_id,
        "<ButtonRelease-1>",
        lambda event, p=players[i]: stop_drag(event, p)
    )

def edit_player(player):
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Player")

    tk.Label(edit_window, text="Name:").pack(pady=5)

    name_entry = tk.Entry(edit_window)
    name_entry.insert(0, player["name"])
    name_entry.pack(pady=5)

    tk.Label(edit_window, text="Number:").pack(pady=5)

    number_entry = tk.Entry(edit_window)
    number_entry.insert(0, player["number"])
    number_entry.pack(pady=5)

    def save_changes():
        player["name"] = name_entry.get()
        player["number"] = number_entry.get()

        pitch.itemconfig(
            player["text_id"],
            text=f"{player['number']}\n{player['name']}"
        )

        edit_window.destroy()

    save_button = tk.Button(
        edit_window,
        text="Save",
        command=save_changes
    )

    save_button.pack(pady=10)

def start_drag(event, player):
    player["dragging"] = True


def drag_player(event, player):
    if player.get("dragging"):
        x = event.x
        y = event.y

        pitch.coords(
            player["circle_id"],
            x - 25,
            y - 25,
            x + 25,
            y + 25
        )

        pitch.coords(
            player["text_id"],
            x,
            y
        )

def update_player_positions():
    positions = formations[formation_var.get()]

    for player in players:
        x, y = positions[player["slot"]]

        pitch.coords(
            player["circle_id"],
            x - 25,
            y - 25,
            x + 25,
            y + 25
        )

        pitch.coords(
            player["text_id"],
            x,
            y
        )

def stop_drag(event, player):
    player["dragging"] = False

    closest_player = None
    closest_distance = 999999

    for other_player in players:
        if other_player == player:
            continue

        other_slot = other_player["slot"]
        other_x, other_y = formations[formation_var.get()][other_slot]

        distance = ((event.x - other_x) ** 2 + (event.y - other_y) ** 2) ** 0.5

        if distance < closest_distance:
            closest_distance = distance
            closest_player = other_player

    if closest_distance < 60:
        player["slot"], closest_player["slot"] = (
            closest_player["slot"],
            player["slot"]
        )

    update_player_positions()


root.mainloop()