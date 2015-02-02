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
model = parse('../obj/african_head.obj')
for facet in model.facets:
    (a, b, c) = map(lambda p: scale(p, (width / 2, height / 2, 0)), map(lambda p: translate(p, (1, 1, 0)), map(lambda id: model.verticies[id], facet)))

    draw_line(img, a, b, White)
    draw_line(img, b, c, White)
    draw_line(img, c, a, White)

write_image(img, '../out/head.tga')



