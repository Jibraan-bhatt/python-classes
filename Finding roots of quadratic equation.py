# Program to find all roots of quadratic equation
import cmath
a=int(input("enter coefficient of x²"))
b=int(input("enter coefficient of x"))
c=int(input("enter any constant"))
D=(b**2)-(4*a*c)
r1=(-b+ cmath.sqrt(D))/(2*a)
r2=(-b- cmath.sqrt(D))/(2*a)
print("the roots of the quadratic equations are",r1,"and",r2)