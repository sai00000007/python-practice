marks=int(input("Enter the Marks(1-100): "))
if marks<=100 and marks>=90:
    print("Grade A")
elif marks<=89 and marks>=75:
    print("Grade B")
elif marks<=74 and marks>=60:
    print("Grade C")
elif marks<=59 and marks>=40:
    print("Grade D")
elif marks<40:
    print("Fail")
else:
    print("Enter valid marks!")