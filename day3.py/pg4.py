age=int(input("Enter your age: "))
if age>=0 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teen")
elif age>=20 and age<=59:
    print("Adult")
elif age>=60:
    print("Senior Citizen")
else:
    print("Enter a valid age!")