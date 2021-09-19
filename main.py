import PIL
from PIL import Image

image_size = 200,200
file_path = str(input(r"Input an image path  EXAMPLE:C:\User\MyAccount\Downloads\Pictures\Sample_Picture.jpg : "))
file_path.encode('unicode_escape')

brightness = ['.', ',', ':', ';', '+', '*', '?', '%', '$', '#', '@']
invert_check = str(input("Do you want to invert color?: "))
if invert_check.lower() == "yes":
    brightness = brightness[::-1]

with Image.open(file_path) as image:
    image.thumbnail(image_size, Image.ANTIALIAS)
    pixels = image.getdata()


def get_luminosity(pxs):
    luminosity = []
    for px in pxs:
        luminosity.append(0.21*px[0] + 0.72*px[1] + 0.07*px[2])
    return luminosity

def turn_to_text(luminosity):
    text = ""
    for px in luminosity:
        index = round(px/23)-1
        text += brightness[index]
        if len(text) >= 200:
            print(text)
            text = ""


pixels_luminosity = get_luminosity(pixels)
turn_to_text(pixels_luminosity)