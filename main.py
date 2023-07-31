# text-based Python program using Pillow package to resize or add text on an image #

from PIL import Image, ImageDraw, ImageFont, ImageColor

FONT = ImageFont.truetype("C:\Windows\Fonts\BRLNSB.TTF", size=40)
RED = (247, 15, 15)


def add_text():
    my_text = input("Enter the text\n")
    entered_color = input("Enter the text color\n")
    text_color = ImageColor.getrgb(entered_color)
    img = Image.open(file_path)
    draw = ImageDraw.Draw(img)
    draw.text((28, 36), text=my_text, fill=text_color, font=FONT)
    img.save(f"images/image.{image_format}")
    img.show()


def resize_image():
    img = Image.open(file_path)
    original_width = img.width
    original_height = img.height
    print(f"Current width is {original_width} and current height is {original_height}")
    new_width = int(input("Enter new width\n"))
    new_height = int(input("Enter new height\n"))
    new_img = img.resize((new_width, new_height))
    new_img.save(f"images/image.{image_format}")
    new_img.show()


file_path = input("Enter file path\n")
image_format = input("Enter desired image format. Type: 'JPG', 'JPEG', 'PNG', 'GIF', 'PNG' \n")
action = input("Type 'resize' to resize the image or 'text' to add a text on the image\n")
if action == "resize":
    resize_image()
elif action == "text":
    add_text()
