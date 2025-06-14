id=int(input("Enter the ID: "))
units=int(input("Enter th no of units: "))
if units<=100:
    print(f"The total amount to be paid = {units*1.5}")
elif units>=101 and units<=200:
    print(f"The total amount to be paid = {units*2.5}")
elif units>=201 and units<=300:
    print(f"The total amount to be paid = {units*4}")
else:
    print(f"The total amount to be paid = {units*6}")

