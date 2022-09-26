no=int(input("enter a number"))
if no%2==0:
    print(no, "is even")
else:
    print(no, "is odd")


x=int(input("enter 1 number"))
y=int(input("enter 2 number"))
z=int(input("enter 3 number"))
if x>=y and x>=z:
    print(x, "is the greatest")
elif y>=x and y>=z:
    print(y,"is the greatest")
else:
    print(z, "is the greatest")


no1=int(input("enter 1 number"))
no2=int(input("enter 2 number"))
no3=int(input("enter 3 number"))
if no1>=no2:
    if no1>=no3:
        print(no1, "is the greatest")
    else:
        print(no3, "is the greatest")
elif no2>=no3:
    print(no2,"is the greatest")
else:
    print(no3,"is the greatest")
