from image import *
from utils import Color
from utils import Point
from utils import White
from utils import Red




img = create_image((100, 100))
set_pixel(img, Point(x=52, y=41), Red)
draw_line(img, Point(13, 20), Point(80, 40), White)
draw_line(img, Point(20, 13), Point(40, 80), Red)
draw_line(img, Point(80, 40), Point(13, 20), Red)
write_image(img, "out.tga")



