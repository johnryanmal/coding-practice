# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

from random import uniform

def point_circle(px, py, x, y, r):
    dx = abs(x - px)
    dy = abs(y - py)
    return (dx*dx + dy*dy <= r*r)


def pi_monte_carlo(iterations):
    points = 0

    for _ in range(iterations):
        #random point in test square (1,1) (-1,1) (-1,-1) (1,-1) which has area of 4
        px = uniform(-1, 1)
        py = uniform(-1, 1)

        #test if point inside unit circle which has area of pi
        if point_circle(px, py, 0, 0, 1):
            points += 1
    
    percentage = points / iterations #estimated pi/4
    return percentage * 4

def estimate_pi(decimals):
    sigfigs = 1 + decimals
    return round(pi_monte_carlo(10 ** sigfigs), decimals)

print(f'{estimate_pi(3):.3f}')