name=input("Enter Your Name: ")
id=input("Enter your ID: ")
n=int(input("Enter Your Marks: "))
if n>=90 or n==100:
    print(f"Hello {name}! Your Grade was 'O' , for your marks{n}")
elif n<90 and n>80:
    print(f"Hello {name}! Your Grade was 'A' , for your marks{n}")
elif n<80 and n>70:
    print(f"Hello {name}! Your Grade was 'B' , for your marks{n}")
elif n<70 and n>60:
    print(f"Hello {name}! Your Grade was 'C' , for your marks{n}")
elif n<60 and n>50:
    print(f"Hello {name}! Your Grade was 'D' , for your marks{n}")
else:
    print(f"Hello {name}! Your Grade was 'F' , for your marks{n} and You are Failed")