physics = int(input("Enter marks of physics:"))
chemistry = int(input("Enter marks of chemistry:"))
biology = int(input("Enter marks of biology:"))
math = int(input("Enter marks of math:"))
computer = int(input("Enter marks of computer:"))
total_marks = physics + chemistry + biology + math + computer
percentage = total_marks/500*100
if percentage >= 33 :
    print(f"Pass with {percentage}%")
    if percentage >= 90:
        print("Grade A") 
    elif percentage >= 80:
        print("Grade B")
    elif percentage >= 70:
        print("Grade C")
    elif percentage >= 60:
        print("Grade D")
    elif percentage >= 50:
        print("Grade E")
    elif percentage >= 40:
        print("Grade F")
    elif percentage >=33:
        print("Grade F+")
else:
    print("FAILED")
   