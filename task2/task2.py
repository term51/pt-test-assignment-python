import math
import sys


def read_circle(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    x, y = map(float, lines[0].split())
    r = float(lines[1])
    return x, y, r


def read_dots(file_path):
    dots = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i >= 100:
                break
            x, y = map(float, line.split())
            dots.append([x, y])

    return dots


def calculate_distance(x0, y0, x, y):
    return math.sqrt((x - x0) ** 2 + (y - y0) ** 2)


def calculate_dots_position():
    circle_path = sys.argv[1]
    dots_path = sys.argv[2]

    center_x, center_y, radius = read_circle(circle_path)
    dots = read_dots(dots_path)

    for dot in dots:
        distance = calculate_distance(center_x, center_y, dot[0], dot[1])
        if distance < radius:
            print(1)
        elif distance == radius:
            print(0)
        else:
            print(2)


calculate_dots_position()
