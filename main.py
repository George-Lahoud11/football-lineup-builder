import tkinter as tk

root = tk.Tk()

root.title("Football Lineup Builder")
root.geometry("900x700")

pitch = tk.Canvas(
    root,
    width=700,
    height=600,
    bg="green"
)

pitch.pack(pady=20)

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


root.mainloop()