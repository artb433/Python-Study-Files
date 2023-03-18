import math
def get_area(shape):
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else: print("Please enter circle or rectangel")
def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    area = length*height
    print("The area of the rectangle is: {:.2f} to two decimal places".format(area))
def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * math.pow(radius, 2)
    print("The area of the circle is: {:.2f} to two decimal places".format(area))
def main():
    shape= input("Enter the name of the shape: ")
    shape = shape.lower()
    get_area(shape)

main()