import tkinter as tk
from formations import formations

def change_formation(*args):
    positions = formations[formation_var.get()]

    for i in range(len(players)):
        x, y = positions[i]

        pitch.coords(
            players[i]["circle_id"],
            x - 25,
            y - 25,
            x + 25,
            y + 25
        )

        pitch.coords(
            players[i]["text_id"],
            x,
            y
        )

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

squad_entry.pack(side="left", padx=5)

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

root.mainloop()