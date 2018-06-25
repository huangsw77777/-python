import math

def quadratic(a, b, c):
    y = ((-b) - math.sqrt(b**2 - 4*a*c)) / (2*a)
    x = ((-b) + math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x,y
