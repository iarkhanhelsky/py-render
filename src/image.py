from PIL import Image

from utils import Black
from utils import Point

def create_image(size):
    '''Create rgba image with given dimentions'''
    img = Image.new("RGBA", size)
    img.paste(Black, (0, 0, size[0], size[1]))
    return img

def write_image(image, file):
    '''Writes image to a given file'''
    image.save(file)

def set_pixel(image, position, color):
    '''Set image pixel color at given position'''
    image.putpixel(position, color)

def draw_line(image, begin, end, color):
    '''Draw straight line begin point to end point'''
    '''with given color'''
    steep = False # if line is steep, we transpose the image
    if abs(begin.x - end.x) < abs(begin.y - end.y) :
        begin = Point(x = begin.y, y = begin.x, z = begin.z)
        end = Point(x = end.y, y = end.x, z = end.z)
        steep = True

    if begin.x > end.x :
        (x, y, _) = begin
        begin = Point(x = end.x, y = end.y, z = begin.z)
        end = Point(x = x, y= y, z = end.z)

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
