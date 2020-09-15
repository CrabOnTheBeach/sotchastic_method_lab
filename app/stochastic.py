from line import Line
import random

def random_point(xlower, xupper, ylower, yupper):
    return (random.uniform(xlower, xupper), random.uniform(ylower, yupper))

def is_inside_all_lines(lines: [Line], point):
    for line in lines:
        if not line.is_inside(point[0], point[1]):
            return False
    return True

#calculate area of shape between all the lines
def area(lines: [Line], xlower, xupper, ylower, yupper):
    points = [random_point(xlower, xupper, ylower, yupper) for _ in range(1000000)]

    count_inside = 0
    for p in points:
        if is_inside_all_lines(lines, p):
            count_inside += 1
    
    square_area = (xupper - xlower) * (yupper - ylower)
    return square_area * (count_inside / len(points))


#integrate the function in shape between all the lines
def integrate(func, lines: [Line], xlower, xupper, ylower, yupper):
    points = [random_point(xlower, xupper, ylower, yupper) for _ in range(1000000)]

    s = 0
    count_inside = 0
    for p in points:
        if is_inside_all_lines(lines, p):
            count_inside += 1
            s += func(p[0], p[1])

    square_area = (xupper - xlower) * (yupper - ylower)
    area = square_area * (count_inside / len(points))
    return (s / count_inside) * area