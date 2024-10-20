#to check whether the triangle is equilateral, isosceles or scalene triangle
x = int(input("Enter any side of triangle:"))
y = int(input("Enter other side of triangle:"))
z = int(input("Enter other side of triangle:"))
if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or z == x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")