a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

if (a > b and a > c) :
    print(a,"has maximum value")
elif (b > a and b > c) :
    print(b,"has maximum value")
else :
    print(c,"has maximum value")