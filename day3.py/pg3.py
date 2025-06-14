n1=int(input("Enter the value : "))
opp=input("Enter the operator: ")
n2=int(input("Enter the value : "))
if opp=='+':
    print(n1+n2)
elif opp=='-':
    print(n1-n2)
elif opp=='*':
    print(n1*n2)
elif opp=='/':
    print(n1/n2)
else:
    print("Enter the valid opperator!")