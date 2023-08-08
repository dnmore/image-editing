from tkinter import *
from PIL import Image, ImageDraw, ImageColor, ImageFont
import numpy as np

FONT = "Tahoma"


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
window.geometry("600x800")
white = Label(window, bg='white', width=600, height=600, border=0)
white.pack()

entry_image = PhotoImage(file="Rectangle 1.png")
button_image = PhotoImage(file="button.png")

# Resize Image

resize_label = Label(text="Resize Image", pady=20, font=(FONT, 12, "bold"), bg="white")
resize_label.place(x=80, y=20)

resize_path_label = Label(text="Enter file path", font=(FONT, 8, "bold"), bg="white")
resize_path_label.place(x=80, y=70)

resize_entry_image = Label(image=entry_image, border=0, bg="white")
resize_entry_image.place(x=200, y=70)
resize_path_entry = Entry(width=30, border=0)
resize_path_entry.place(x=204, y=74)

new_width_label = Label(text="Enter new width", font=(FONT, 8, "bold"), bg="white")
new_width_label.place(x=80, y=120)
width_entry_image = Label(image=entry_image, border=0, bg="white")
width_entry_image.place(x=200, y=120)
new_width_entry = Entry(width=30, border=0)
new_width_entry.place(x=204, y=124)

new_height_label = Label(text="Enter new height", font=(FONT, 8, "bold"), bg="white")
new_height_label.place(x=80, y=170)
height_entry_image = Label(image=entry_image, border=0, bg="white")
height_entry_image.place(x=200, y=170)
new_height_entry = Entry(width=30, border=0)
new_height_entry.place(x=204, y=174)
resize_button = Button(image=button_image, borderwidth=0, bg="white", cursor="hand2", command=resize_image)
resize_button.place(x=80, y=200)

# Add Text

add_text_label = Label(text="Add Text", pady=20, font=(FONT, 12, "bold"), bg="white")
add_text_label.place(x=80, y=270)

text_path_label = Label(text="Enter file path", font=(FONT, 8, "bold"), bg="white")
text_path_label.place(x=80, y=320)
text_path_image = Label(image=entry_image, border=0, bg="white")
text_path_image.place(x=200, y=320)
text_path_entry = Entry(width=30, border=0)
text_path_entry.place(x=204, y=324)

text_label = Label(text="Enter Text", font=(FONT, 8, "bold"), bg="white")
text_label.place(x=80, y=370)
text_entry_image = Label(image=entry_image, border=0, bg="white")
text_entry_image.place(x=200, y=370)
text_entry = Entry(width=30, border=0)
text_entry.place(x=204, y=374)

color_label = Label(text="Enter Color", font=(FONT, 8, "bold"), bg="white")
color_label.place(x=80, y=420)
color_entry_image = Label(image=entry_image, border=0, bg="white")
color_entry_image.place(x=200, y=420)
color_entry = Entry(width=30, border=0)
color_entry.place(x=204, y=424)
add_text_button = Button(image=button_image, borderwidth=0, bg="white", cursor="hand2", command=add_text)
add_text_button.place(x=80, y=454)

# Convert Gray Scale

gray_label = Label(text="Convert to Gray Scale", pady=20, font=(FONT, 12, "bold"), bg="white")
gray_label.place(x=80, y=504)

path_label = Label(text="Enter file path", font=(FONT, 8, "bold"), bg="white")
path_label.place(x=80, y=554)
gray_path_image = Label(image=entry_image, border=0, bg="white")
gray_path_image.place(x=200, y=554)
gray_path_entry = Entry(width=30, border=0)
gray_path_entry.place(x=204, y=558)

convert_gray_button = Button(image=button_image, borderwidth=0, bg="white", cursor="hand2", command=convert_grayscale)
convert_gray_button.place(x=80, y=588)

window.mainloop()


