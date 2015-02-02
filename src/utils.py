from functools import namedtuple

'''Handy helper for independent color implementation'''
Color = namedtuple("Color", "red green blue alpha")

'''Handy helper for independent point implementation'''
Point = namedtuple("Point", "x y z")


'''Color constants'''
White = Color(red = 255, green = 255, blue = 255, alpha = 255)
Red   = Color(red = 255, green = 0, blue = 0, alpha = 255)
Black = Color(red = 0, green = 0, blue = 0, alpha = 255)


def scale(point, scale):
    return Point(x = int(point.x * scale[0]), y = int(point.y * scale[1]), z = int(point.z * scale[2]))

def translate(point, move):
    return Point(point.x + move[0], point.y + move[1], point.z + move[2])
