from functools import partial
from itertools import combinations

from image import *

from utils import Color
from utils import Point
from utils import White
from utils import Red

from utils import scale
from utils import translate

from model import parse


(width, height) = (500, 500)
img = create_image((width, height))
draw_triangle(img, (Point(10, 10, 0), Point(10, 490, 0), Point(490, 490, 0)), (255, 100, 128))
write_image(img, '../out/triangles.tga')
