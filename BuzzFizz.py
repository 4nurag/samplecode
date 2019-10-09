##For each multiple of 3, print "Fizz" instead of the number. 
##
##For each multiple of 5, print "Buzz" instead of the number. 
##
##For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

a = int(input("enter a number="))
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a%3==0:
    print("Fizz")
elif a%5==0:
    print("Buzz")
else:
    print("Not Define")
