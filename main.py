import tkinter as tk
from formations import formations
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

def change_formation(*args):
    update_player_positions()

def update_squad_name(event=None):
    name = squad_entry.get()

    if name.strip() == "":
        squad_heading.config(text="My Squad")
    else:
        squad_heading.config(text=name)

def reset_lineup():
    for i in range(len(players)):
        players[i]["slot"] = i

    update_player_positions()

def export_lineup():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save Lineup"
    )

    if not file_path:
        return

    # Create image
    image = Image.new(
        "RGB",
        (700, 700),
        "white"
    )

    draw = ImageDraw.Draw(image)

    # Fonts
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 28)
        player_font = ImageFont.truetype("arial.ttf", 13)
        position_font = ImageFont.truetype("arial.ttf", 12)
        formation_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        player_font = ImageFont.load_default()
        position_font = ImageFont.load_default()
        formation_font = ImageFont.load_default()

    # Squad heading
    squad_name = squad_entry.get().strip()

    if squad_name == "":
        squad_name = "My Squad"

    draw.text(
        (350, 25),
        squad_name,
        fill="black",
        font=title_font,
        anchor="mm"
    )

    # Formation
    draw.text(
        (350, 55),
        formation_var.get(),
        fill="black",
        font=formation_font,
        anchor="mm"
    )

    # Pitch starts lower because of heading
    offset_y = 80

    # Pitch background
    draw.rectangle(
        (0, offset_y, 700, 680),
        fill="#238636"
    )

    # Outer boundary
    draw.rectangle(
        (20, 20 + offset_y, 680, 580 + offset_y),
        outline="white",
        width=3
    )

    # Halfway line
    draw.line(
        (20, 300 + offset_y, 680, 300 + offset_y),
        fill="white",
        width=3
    )

    # Centre circle
    draw.ellipse(
        (300, 250 + offset_y, 400, 350 + offset_y),
        outline="white",
        width=3
    )

    # Top penalty box
    draw.rectangle(
        (220, 20 + offset_y, 480, 120 + offset_y),
        outline="white",
        width=3
    )

    # Bottom penalty box
    draw.rectangle(
        (220, 480 + offset_y, 480, 580 + offset_y),
        outline="white",
        width=3
    )

    positions = formations[formation_var.get()]

    # Draw players
    for player in players:
        slot = positions[player["slot"]]

        x, y = slot["coords"]
        position = slot["position"]

        y += offset_y

        # Player circle
        draw.ellipse(
            (x - 25, y - 25, x + 25, y + 25),
            fill="#7D2136",
            outline="white",
            width=2
        )

        # Shirt number
        draw.text(
            (x, y),
            str(player["number"]),
            fill="white",
            font=player_font,
            anchor="mm"
        )

        # Player name
        draw.text(
            (x, y + 34),
            player["name"],
            fill="white",
            font=player_font,
            anchor="mm"
        )

        # Position
        draw.text(
            (x, y + 50),
            position,
            fill="white",
            font=position_font,
            anchor="mm"
        )

    # Centre spot
    draw.ellipse(
        (
            346,
            296 + offset_y,
            354,
            304 + offset_y
        ),
        fill="white"
    )

    # Top goal
    draw.rectangle(
        (300, 5 + offset_y, 400, 20 + offset_y),
        outline="white",
        width=3
    )

    # Bottom goal
    draw.rectangle(
        (300, 580 + offset_y, 400, 595 + offset_y),
        outline="white",
        width=3
    )

    image.save(file_path)

    draw.ellipse(
    (
        346,
        296 + offset_y,
        354,
        304 + offset_y
            ),
        fill="white"
    )

    # Top goal
    draw.rectangle(
        (300, 5 + offset_y, 400, 20 + offset_y),
        outline="white",
        width=3
    )

    # Bottom goal
    draw.rectangle(
        (300, 580 + offset_y, 400, 595 + offset_y),
        outline="white",
        width=3
    )

    image.save(file_path)

root = tk.Tk()

root.title("Football Lineup Builder")
root.geometry("900x700")

controls = tk.Frame(root)
controls.pack(pady=10)

reset_button = tk.Button(
    controls,
    text="Reset Lineup",
    command=reset_lineup
)

reset_button.pack(side="left", padx=5)

export_button = tk.Button(
    controls,
    text="Export Image",
    command=export_lineup
)

export_button.pack(side="left", padx=5)

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
    *formations.keys()
)

formation_menu.pack(side="left", padx=5)

pitch = tk.Canvas(
    root,
    width=700,
    height=600,
    bg="#238636"
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
    {"name": "Player 1", "number": 1},
    {"name": "Player 2", "number": 2},
    {"name": "Player 3", "number": 3},
    {"name": "Player 4", "number": 4},
    {"name": "Player 5", "number": 5},
    {"name": "Player 6", "number": 6},
    {"name": "Player 7", "number": 7},
    {"name": "Player 8", "number": 8},
    {"name": "Player 9", "number": 9},
    {"name": "Player 10", "number": 10},
    {"name": "Player 11", "number": 11}
]

positions = formations["4-3-3"]

for i in range(len(players)):
    slot = positions[i]

    x, y = slot["coords"]
    position = slot["position"]

    circle_id = pitch.create_oval(
        x - 25,
        y - 25,
        x + 25,
        y + 25,
        fill="#7D2136",
        outline="white",
        width=2
    )

    text_id = pitch.create_text(
        x,
        y,
        text=f"{players[i]['number']}\n{players[i]['name']}",
        fill="white",
        font=("Arial", 9, "bold")
    )

    position_id = pitch.create_text(
        x,
        y + 35,
        text=position,
        fill="white",
        font=("Arial", 8)
    )

    players[i]["circle_id"] = circle_id
    players[i]["text_id"] = text_id
    players[i]["slot"] = i
    players[i]["position_id"] = position_id

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

        pitch.coords(
            player["position_id"],
            x,
            y + 35
        )


def update_player_positions():
    positions = formations[formation_var.get()]

    for player in players:
        slot = positions[player["slot"]]

        x, y = slot["coords"]
        position = slot["position"]

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

        pitch.coords(
            player["position_id"],
            x,
            y + 35
        )

        pitch.itemconfig(
            player["position_id"],
            text=position
        )

def stop_drag(event, player):
    player["dragging"] = False

    closest_player = None
    closest_distance = 999999

    for other_player in players:
        if other_player == player:
            continue

        other_slot = other_player["slot"]

        other_position = formations[formation_var.get()][other_slot]

        other_x, other_y = other_position["coords"]

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