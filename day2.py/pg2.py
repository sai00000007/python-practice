n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 and n1>n3:
    print(f"{n1} is the Big")
elif n2>n1 and n2>n3:
    print(f"{n2} is the Big")
else:
    print(f"{n3} is the Big")