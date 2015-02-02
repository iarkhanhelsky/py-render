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

def draw_line(image, begin, end, color):
    '''Draw straight line begin point to end point'''
    '''with given color'''
    steep = False # if line is steep, we transpose the image
    if abs(begin.x - end.x) < abs(begin.y - end.y) :
        begin = Point(x = begin.y, y = begin.x)
        end = Point(x = end.y, y = end.x)
        steep = True

    if begin.x > end.x :
        (x, y) = begin
        begin = Point(x = end.x, y = end.y)
        end = Point(x = x, y= y)

    (dx, dy) = (end.x - begin.x, end.y - begin.y)
    derror = abs(dy/dx)
    error = 0
    y = begin.y

    for x in range(begin.x, end.x):
        set_pixel(image, (y, x) if steep else (x, y), color)
        error = error + derror
        if error > 0.5:
            y = y + (1 if end.y > begin.y else -1)
            error = error - 1


img = create_image((100, 100))
set_pixel(img, Point(x=52, y=41), red)
draw_line(img, Point(13, 20), Point(80, 40), white)
draw_line(img, Point(20, 13), Point(40, 80), red)
draw_line(img, Point(80, 40), Point(13, 20), red)
write_image(img, "out.tga")



