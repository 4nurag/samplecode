num = int(input("enter a number="))
s = 0
a = num
while(num>0):
    dg = num%10
    s = s+dg**3
    num = num//10
if a==s:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
