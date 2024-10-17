number = int(input("Enter the number:"))
if number%5==0 and number%11!=0:
    print(f"{number} is divisible by 5 but not by 11")
elif number%5==0 and number%11==0:
    print(f"{number} is divisible by both 5 and 11")
elif number%5!=0 and number%11==0:
    print(f"{number} is divisible by 11 but not by 5")
else:
    print(f"{number} is neither divisible by 5 nor 11")