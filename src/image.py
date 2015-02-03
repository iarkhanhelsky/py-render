from PIL import Image

from itertools import combinations
from functools import partial

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
    p = (position[0], image.size[1] - position[1])
    try:
        image.putpixel(p, color)
    except IndexError:
        print(p)
        raise


def draw_line(image, begin, end, color):
    '''Draw straight line begin point to end point'''
    '''with given color'''
    if not (begin.x == end.x and begin.y == end.y):
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

def fill_triangle(image, points, color):
    assert(len(points) is 3)
    mid = (points[2][0] - points[0][0], points[2][1] - points[0][1])
    mid = Point(mid[0], mid[1], 0)
    if not abs(mid[0] - points[0][0]) < 1:
        draw_line(image, points[1], mid, color)
        fill_triangle(image, (points[0], mid, points[2]), color)
        fill_triangle(image, (mid, points[1], points[2]), color)

def draw_triangle(image, points, color, filled=True):
    '''Draw triangle with lines of given color'''
    assert(len(points) is 3)

    for segment in combinations(points, 2):
        draw_line(image, segment[0], segment[1], color)

    if filled:
        fill_triangle(image, sorted(points, key=partial(lambda x,y: x[y], y=0)), color)
