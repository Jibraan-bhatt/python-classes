#To check validity of a triangle based on given sides
side1=int(input("Enter first side:"))
side2=int(input("Enter second side:"))
side3=int(input("Enter third side:"))
property1=side1+side2
property2=side2+side3
property3=side1+side3

if (property1 > side3 or property2 > side1 or property3 > side2) :
    print("The given triangle is valid.")
else :
    print("The given triangle is not valid.")