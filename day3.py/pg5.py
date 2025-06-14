n=int(input("Enter a Year: "))
if n%4==0 and n%100!=0 or n%400==0:
    print("Leap Year!")
    if n%5==0:
        print("divisible by 5✅")
    else:
        print("Not divisible by 5❌")
else :
    print("Not a Leap Year!")