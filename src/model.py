from functools import namedtuple
import re

from utils import Point


Model = namedtuple("Model", "facets verticies")

def parse(file):

    facets = []
    verticies = []

    for line in open(file):
        if (re.match('v .*', line)):
            point = list(map(float, parse_floats(line)))
            verticies.append(Point(x = point[0], y = point[1], z = point[2]))
        elif (re.match('f .*', line)):
            facets.append(map(int, map(lambda tri: re.findall('\d+', tri)[0], re.findall('\d+\/\d+\/\d+', line))))

    return Model(facets, verticies)


def parse_floats(line):
    float_rx = '[+-]?(?:(?:\d+)?\.?\d+)(?:[eE][+-]\d+)?'
    return list(map(float, re.findall(float_rx, line)))


if '__main__' == __name__:
    #print(parse_floats('1 -1 1.0 0.123 0.1234e-24'))
    assert all([ abs(x - y) < 0.00000001 for x in parse_floats('1 -1 1.0 0.123 0.1234e-24') for y in [1, -1, 1, 0.123, 0.123e-24]])

