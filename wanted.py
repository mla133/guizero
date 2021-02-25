from guizero import App, Text, Picture

app = App("Wanted!")
app.bg = "#FBFBD0"

wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text.text_font = "Courier"

buddy = Picture(app, image="pearl.png")
app.display()

