import cmath
import math
import sys

SQUARED = "\N{SUPERSCRIPT TWO}" # @ Linux or Mac OS
ARROW = "\N{RIGHTWARDS ARROW}"  # @ Linux or Mac OS

if sys.platform.startswith("win"):
    SQUARED = '^2'
    ARROW = '->'

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

print("ax" + SQUARED + " + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("entec c: ", True)

x1 = None
x2 = None

discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

#equation = ("{0}x{1} + {2}x + {3} = 0"
#            "{4} x = {5}").format(a, SQUARED, b, c, ARROW, x1)
# or
equation  = ("{a}x{SQUARED} + {b}x + {c} = 0 {ARROW} x = {x1}").format(**locals())


if x2 is not None:
    equation += " or x = {0}".format(x2)
print(equation)
