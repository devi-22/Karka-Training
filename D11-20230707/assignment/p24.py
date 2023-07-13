#Find area of a triangle using Heron's formula
def area_of_triangle():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    s=(a+b+c)/2
    area_of_triangle=(s*((s-a)*(s-b)*(s-c)))**(1/2)
    print(area_of_triangle)
area_of_triangle()
#Find area of square
def area_of_square():
    a=int(input("a="))
    area_of_square=(a**2)
    print(area_of_square)
area_of_square()
#Find area of rectangle
def area_of_rectangle():
    length=int(input("length="))
    width=int(input("width="))
    area_of_rectangle=(width*length)
    print(area_of_rectangle)
area_of_rectangle()
#Find area of circle
def area_of_circle():
    radius=int(input("radius="))
    area_of_circle=(3.14*radius**2)
    print(area_of_circle)
area_of_circle()
#Find area of trapezium:
def area_of_trapezium():
    a=int(input("base="))
    b=int(input("base="))
    c=int(input("height="))
    area_of_trapezium=((a+b)/2)*c
    print(area_of_trapezium)
area_of_trapezium()





    

    
