#To check if a Character is an alphabet, digit or special character
c=input("Enter any character: ")

if (c >='a' and c <='z' or c >='A' and c <='Z' ) :
    print(c,"is an alphabet.")
elif (c>='0' and c<='9') :
    print(c,"is a digit.")
else :
    print(c,"is a special character.")