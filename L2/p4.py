a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))

if(a>=b and a>=c and a>=d):
    print("leargest a",a)
elif(b>=a and b>=c and b>=d):
    print("greater b", b)
elif(c>=1 and c>=b and c>=d):
    print("c is leargest", c)
else:
    print("d is greater ",d)