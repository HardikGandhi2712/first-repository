no=int(input("write the no till u want sum"))
sum=0
for i in range(1,no+1):
    sum=sum+i
print(sum)

no1=int(input("write the no till u want productt"))
product=1
for i in range(1,no1+1):
    product=product*i
    print("ran") #debugging
print(product)

no2=int(input("write the number u want the square of"))
square=0
for i in range(1,no2+1):
    square=no2+square
print(square)

count=0
for x in range(1,10+1):
    if x%2==0:
        count=count+1
        print(x)
print("we have",count,"even no.")


i=1
while i<=5:
    print(i * '*')
    i=i+1
