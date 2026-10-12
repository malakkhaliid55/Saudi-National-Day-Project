import tkinter as tk
import random
root = tk.Tk()
root.title("اليوم الوطني السعودي")
root.geometry("800x600")
root.configure(bg="#064E3B")
canvas = tk.Canvas(
    root,
    width=800,
    height=600,
    bg="#064E3B",
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)
canvas.create_text(
    400, 70,
    text="اليوم الوطني السعودي",
    font=("Arial", 30, "bold"),
    fill="white"
)
canvas.create_rectangle(
    180, 150, 620, 340,
    fill="#006C35",
    outline="#006C35"
)
canvas.create_text(
    400, 220,
    text="لا إله إلا الله محمد رسول الله",
    font=("Arial", 24, "bold"),
    fill="white"
)
canvas.create_polygon(
    290, 280,
    310, 274,
    500, 274,
    500, 286,
    310, 286,
    fill="white",
    outline="white"
)
canvas.create_line(
    500, 280,
    520, 280,
    fill="white",
    width=5
)
canvas.create_line(
    490, 268,
    490, 292,
    fill="white",
    width=4
)
canvas.create_text(
    400, 410,
    text="دام عزك يا وطن",
    font=("Arial", 38, "bold"),
    fill="#FACC15"
)
canvas.create_text(
    400, 470,
    text="كل عام والمملكة العربية السعودية بخير",
    font=("Arial", 20),
    fill="white"
)

stars = []
for _ in range(40):
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    star = canvas.create_text(
        x, y,
        text="✦",
        fill="#FACC15",
        font=("Arial", random.randint(12, 24))
    )
    stars.append(star)
def move_stars():
    for star in stars:
        canvas.move(star, 0, 2)
        x, y = canvas.coords(star)
        if y > 610:
            canvas.coords(
                star,
                random.randint(10, 790),
                -10
            )
    root.after(50, move_stars)
move_stars()
root.mainloop()