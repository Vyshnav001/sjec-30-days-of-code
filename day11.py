import math

p = int(input("Enter the radius of the circle"))
q = int(input("Enter a side of a square"))
r = int(input("Enter the side of an equilateral triangle"))
s = int(input("Enter the length of the rectangle"))
t = int(input("Enter the breath of the rectangle"))



circle_radius =p
circle_area = math.pi * circle_radius**2


square_side = q
square_area = square_side**2

triangle_side = r
triangle_are = (math.sqrt(3)/4) * triangle_side**2


rectangle_length = s
rectangle_breath = t
rectangle_area = rectangle_length * rectangle_breath


shapes = {
    "Circle": circle_area,
    "Square": square_area,
    "Triangle": triangle_are,
    "Rectangle": rectangle_area
}


sorted_shape = sorted(shapes.items(), key = lambda x: x[1], reverse=True)

for shape, area in sorted_shape:
    print(f"{shape}")

