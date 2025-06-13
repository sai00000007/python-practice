n1=int(input("Enter a Number: "))
n2=int(input("Enter a Number: "))
ac=input("Enter the operator: ")
if ac=='+':
    print(n1+n2)
elif ac=='-':
    print(n1-n2)
elif ac=='*':
    print(n1*n2)
elif ac=='/':
    print(n1/n2)
else:
    print("Enter a valid operator")