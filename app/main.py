from parabola import Parabola
import visualizer
import math
import stochastic



def getdata():
    parabolas = []
    n = int(input())
    for i in range(n):
        a, move_x, move_y, rotation = map(float, input().split())
        p = Parabola(a, move_x, move_y, rotation)
        parabolas.append(p)
    return parabolas

def test(par):
    p = (5, 5)
    p1 = par.transform(p[0], p[1])
    print(p1)
    p2 = par.back_transform(p1[0], p1[1])
    print(p2)




parabolas = getdata()
test(parabolas[0])
visualizer.visualize(parabolas)
print(stochastic.area(parabolas, -10, 10, -10, 10))
print(stochastic.integrate(lambda x, y: x**2 * y**2, parabolas, -10, 10, -10, 10))

#save(x, 'x', y, 'y(x)')