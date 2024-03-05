from tkinter import *
from PIL import Image, ImageDraw, ImageColor, ImageFont
import numpy as np

FONT = "Arial"


def add_text():
    my_text = text_entry.get()
    entered_color = color_entry.get()
    text_color = ImageColor.getrgb(entered_color)
    img = Image.open(text_path_entry.get())
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((28, 36), text=my_text, fill=text_color, font=font)
    img.save("image.png")
    img.show()


def resize_image():
    img = Image.open(resize_path_entry.get())
    new_width = int(new_width_entry.get())
    new_height = int(new_height_entry.get())
    new_img = img.resize((new_width, new_height))
    new_img.save("image.png")
    new_img.show()


def convert_grayscale():
    img_gray = np.array(Image.open(gray_path_entry.get()).convert("L"))
    new_img = Image.fromarray(img_gray)
    new_img.save("image.png")
    new_img.show()


# ------ UI SET UP -----#

window = Tk()
window.title("Image Editing App")
window.geometry("600x600")
white = Label(window, bg='white', width=600, height=600, border=0)
white.pack()

# Labels #

resize_label = Label(text="Resize Image", pady=20, font=(FONT, 12, "bold"), bg="white")
resize_label.place(x=80, y=20)
resize_path_label = Label(text="Enter file path", font=(FONT, 8, "bold"), bg="white")
resize_path_label.place(x=80, y=70)
new_width_label = Label(text="Enter new width", font=(FONT, 8, "bold"), bg="white")
new_width_label.place(x=80, y=120)
new_height_label = Label(text="Enter new height", font=(FONT, 8, "bold"), bg="white")
new_height_label.place(x=80, y=170)
add_text_label = Label(text="Add Text", pady=20, font=(FONT, 12, "bold"), bg="white")
add_text_label.place(x=80, y=270)
text_path_label = Label(text="Enter file path", font=(FONT, 8, "bold"), bg="white")
text_path_label.place(x=80, y=320)
text_label = Label(text="Enter Text", font=(FONT, 8, "bold"), bg="white")
text_label.place(x=80, y=370)
color_label = Label(text="Enter Color", font=(FONT, 8, "bold"), bg="white")
color_label.place(x=80, y=420)
gray_label = Label(text="Convert to Gray Scale", pady=20, font=(FONT, 12, "bold"), bg="white")
gray_label.place(x=80, y=504)
path_label = Label(text="Enter file path", font=(FONT, 8, "bold"), bg="white")
path_label.place(x=80, y=554)

# Entries #

resize_path_entry = Entry(width=35, borderwidth=2)
resize_path_entry.place(x=204, y=74)
resize_path_entry.focus()
new_width_entry = Entry(width=35, borderwidth=2)
new_width_entry.place(x=204, y=124)
new_height_entry = Entry(width=35, borderwidth=2)
new_height_entry.place(x=204, y=174)
text_path_entry = Entry(width=35, borderwidth=2)
text_path_entry.place(x=204, y=324)
text_entry = Entry(width=35, borderwidth=2)
text_entry.place(x=204, y=374)
color_entry = Entry(width=35, borderwidth=2)
color_entry.place(x=204, y=424)
gray_path_entry = Entry(width=35, borderwidth=2)
gray_path_entry.place(x=204, y=558)


# Buttons #
resize_button = Button(text="Resize", width=10, borderwidth=1, bg="antiquewhite2", cursor="hand2", command=resize_image)
resize_button.place(x=80, y=200)
add_text_button = Button(text="Add Text", width=10, borderwidth=1, bg="antiquewhite2", cursor="hand2", command=add_text)
add_text_button.place(x=80, y=454)
convert_gray_button = Button(text="Convert", width=10, borderwidth=1, bg="antiquewhite2", cursor="hand2", command=convert_grayscale)
convert_gray_button.place(x=80, y=588)

window.mainloop()


