from parabola import Parabola
import matplotlib.pyplot as plt
import stochastic


def args_from_range(fr, to, dx):
    return [fr + i * dx for i in range(int(1 + (to - fr) / dx))]


def transformed_points(func, args):
    xy = [func(arg) for arg in args]
    x = [elem[0] for elem in xy]
    y = [elem[1] for elem in xy]
    return x, y


def visualize(parabolas):
    for p in parabolas:
        args = args_from_range(-5, 5, 0.01)
        x, y = transformed_points(p.transformed_point, args)
        plt.plot(x, y, label=f'y = {p.a} * x ** 2 moved to ({p.move_x}, {p.move_y}), rotated to {p.rotation} radian') 

    plt.legend(bbox_to_anchor=(0, 1.1), loc='upper left')

    points = [stochastic.random_point(-10, 10, -10, 10) for _ in range(2500)]
    for p in points:
        if stochastic.is_inside_all_lines(parabolas, p):
            plt.scatter(p[0], p[1], s=10, color="magenta")
        else:
            plt.scatter(p[0], p[1], s=10, color="purple")

    #draw square
    x = args_from_range(-10, 10, 0.1)
    y = [-10 for _ in range(len(x))]

    plt.plot(x, y, color="black")
    plt.plot(y, x, color="black")
    y = list(map(lambda x: -x, y))

    plt.plot(x, y, color="black")
    plt.plot(y, x, color="black")

    
    plt.savefig('figure')
