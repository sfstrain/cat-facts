import tkinter as tk
import requests
from PIL import Image, ImageTk


def get_catfact():
    response = requests.get(url=catfacts_url)
    response.raise_for_status()
    data = response.json()
    catfact = data["fact"]
    canvas.itemconfig(catfact_text, text=catfact)


catfacts_url = "https://catfact.ninja/fact"

window = tk.Tk()
window.title("Ninja Cat Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=416, height=311)
image = Image.open("blackboard.jpg")
background_img = ImageTk.PhotoImage(image)
canvas.create_image(208, 155, image=background_img)
catfact_text = canvas.create_text(208, 100, text="", width=250, font=("Arial", 12, "bold"), fill="white")
canvas.grid(row=0, column=0)

image = Image.open("ninja_cat.jpg")
ninjacat_img = ImageTk.PhotoImage(image)
ninjacat_button = tk.Button(image=ninjacat_img, highlightthickness=0, command=get_catfact)
ninjacat_button.grid(row=1, column=0)

window.mainloop()
