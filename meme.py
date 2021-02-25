# Imports -----------------------
from guizero import App, TextBox, Drawing, Combo, Slider
import os, sys

# Functions ---------------------
def draw_meme():
    meme.clear()
    meme.image(0,0,image=image.value)
    meme.text(20,20, top_text.value, color=color1.value, size=size1.value, font="courier")
    meme.text(20,320, bottom_text.value, color=color2.value, size=size2.value, font="times new roman")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

# App ---------------------------
app = App("meme")

top_text = TextBox(app, "top_text", command=draw_meme)
bottom_text = TextBox(app, "bottom_text", command=draw_meme)

color1 = Combo(app, options = ["black", "white", "red", "green", "blue", "orange"], command=draw_meme, selected="blue")
color2 = Combo(app, options = ["black", "white", "red", "green", "blue", "orange"], command=draw_meme, selected="blue")
size1  = Slider(app, start=20, end=40, command=draw_meme)
size2  = Slider(app, start=20, end=40, command=draw_meme)

image  = Combo(app, options = [resource_path("assets\\pearl.png"), resource_path("assets\\buddy.png")], command=draw_meme, selected=resource_path("assets\pearl.png"))

meme = Drawing(app, width="fill", height="fill")

draw_meme()
app.display()


