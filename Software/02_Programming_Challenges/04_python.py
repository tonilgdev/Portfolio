"""
 * Create a single function (it is important that it is only one) that is able to
 * to calculate and return the area of a polygon.
 * The function will receive by parameter only ONE polygon at a time.
 * The polygons supported will be Triangle, Square and Rectangle.
 * - Print the calculation of the area of one polygon of each type.
"""

def polygon_area (pol, *param):
    if pol == "Triangle":
        print(f"The area of your triangle is {param[0]*param[1]*0.5}")
    elif pol == "Square":
        print(f"The area of your square is {param[0]**2}")
    elif pol == "Rectangle":
        print(f"The area of your rectangle is {param[0]*param[1]}")
    else:
        print("This polygon is not allowed")

polygon_area("Triangle", 4, 5)
polygon_area("Square", 4)
polygon_area("Rectangle", 4, 8)
polygon_area("Pentagon")