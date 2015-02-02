from PIL import Image
from functools import namedtuple

'''Handy helper for independent color implementation'''
Color = namedtuple("Color", "red green blue alpha")

'''Handy helper for independent point implementation'''
Point = namedtuple("Point", "x y")

'''Color constants'''
white = Color(red = 255, green = 255, blue = 255, alpha = 255)
red   = Color(red = 255, green = 0, blue = 0, alpha = 255)
black = Color(red = 0, green = 0, blue = 0, alpha = 255)


def create_image(size):
    '''Create rgba image with given dimentions'''
    img = Image.new("RGBA", size)
    img.paste(black, (0, 0, size[0], size[1]))
    return img

def set_pixel(image, position, color):
    '''Set image pixel color at given position'''
    image.putpixel(position, color)

def write_image(image, file):
    '''Writes image to a given file'''
    image.save(file)

img = create_image((100, 100))
set_pixel(img, Point(x=52, y=41), red)
write_image(img, "out.tga")
