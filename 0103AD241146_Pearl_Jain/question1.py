#1.WAP swap numbers without using third variable
#usind tuple unpacking

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

a,b = b,a

print(a,b)
