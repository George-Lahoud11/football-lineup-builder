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

root.mainloop()