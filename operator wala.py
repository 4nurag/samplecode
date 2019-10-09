a = float(input("enter the first number="))
b = float(input("enter the second number="))
c = input("enter the operator=")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="**":
    print(a**b)
elif c=="//":
    print(a//b)
elif c=="%":
    print(a%b)
else:
    print("invalid operator")
