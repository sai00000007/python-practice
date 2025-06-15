n=int(input("Enter a number: "))
k=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n//=10
if rev==k:
    print("Palindrome")
else :
    print("Not a palindrome")