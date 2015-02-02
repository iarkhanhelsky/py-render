from functools import namedtuple
import re

from utils import Point

float_rx = '[+-]?((?\d+)|(\d+\.\d+))(?[eE][+-]?\d+)'

Model = namedtuple("Model", "facets verticies")

def flt(f):
    print(f)
    return float(f)

def parse(file):

    facets = []
    verticies = []

    for line in open(file):
        if (re.match('v .*', line)):
            point = [flt(f) for f in re.findall(float_rx, line)]
            verticies.append(Point(x = point[0], y = point[1], z = point[2]))
        elif (re.match('f .*', line)):
            facets.append(map(int, map(lambda tri: re.findall('\d+', tri)[0], re.findall('\d+\/\d+\/\d+', line))))

    return Model(facets, verticies)
