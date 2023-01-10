
x=5
y=2
print(x%y)
print(x//y)
print(x**y)

if x>y:
    print("x is greater than y")
else:
    print("y is greater is x")

#This is a comment
"""
Multiline comment
"""
a=int(input("write 1 num"))
b=str(input("write 2."))
print(a,b)
lst=[a,b]
print(lst)
print([a,b])
mnq="eqfer"
print(list(mnq))
print(tuple(mnq))
print(set(mnq))
pqr={2:"Hi", 3:"Bye"}
print(pqr[3])

xyz={2,3,3,2}
print(xyz)

for x in "banana":
    print (x)
print()

z=["ASD","DAS","FDG"]
for x in z:
    print (x)
print()

for x in range (0,10):
    print (x)
print()

for x in range (0,10,2):
    print (x)
print()

m={2:"HI",3:"xd"}
for x in m:
    print (m[x])
    for y in m[x]:
        print(y)
print()
m={"ds":2,"cx":4}
for x in m:
    print(m[x])
    for y in range(0,m[x]):
        print(y)
        for z in (x):
            print(z)
print()

for x in range(0,6):
    print(x)
else:
    print("You")
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) 
    if x == "banana":
        break
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
    print("xx")
print()
    
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
for x in range(len(fruits)):
	print(fruits[x])

sda=[1,2,3,4,5]
dad=[["fd",21],["dsaf",32]]
print(dad[1][0])
print(dict(dad))

print(0%2)

n01=10
print(n01>15 and n01%2)

print(3&2)

print(3|2)

print(3^2)

print(3<<1)

print(3>>1)

no=5
print(id(no))

num=5
print(id(num))
print(no is num)
print (no is not num)

o=22
o+=5
print(o)

o-=5
print(o)

o=o//3
print(o)

no=int(input("write the number you want the product of"))
product=1
i=1
while(i<=no):
    product=product*i
    i=i+1
print(product)

d = {1: "jfr", 2: "rewj", 3: "ojor4j"}
for key, val in d.items():
    print(key, val)

x=int(input("write your marks"))
if x>=60:
    print("Distinction")
    if x>80:
        print("Topper")
else:
    print("Failure")

#3 methods for table
table=3
for x in range(1,11):
    print(table*x)

num=4
y=0
for x in range(1,11):
    y=y+num
    print(y)

num1=int(input("write the table"))
for x in range(num1,num1*10+1,num1):
    print(x)


i=1
num2=int(input("input"))
while i<=10:
    print(num2*i)
    i=i+1

i=1
z=0
table=5
while i<=10:
    z=z+table
    print(z)
    i=i+1
'''
'''
num=int(input("write 1 number"))
num1=int(input("write 2 number"))
count=0
for x in range(num,num1+1):
    if x%4==0:
        count=count+1
        print(x)
print(count)

num=int(input("write 1 number"))
num1=int(input("write 2 number"))
count=0
while num<=num1+1:
    if num%4==0:
        count=count+1
        print(num)
    num=num+1
print(count)

num=int(input("write 1 number"))
num1=int(input("write 2 number"))
count=0
for x in range(num,num1-1,-1):
    if x%4==0:
        count=count+1
        print(x)
print(count)

num=int(input("write 1 number"))
num1=int(input("write 2 number"))
count=0
while num>=num1-1:
    if num%4==0:
        count=count+1
        print(num)
    num=num-1
print(count)

num1=int(input("write the base"))
num2=int(input("Write the power"))
i=1
ans=1
while i<=num2:
    ans=ans*num1
    i=i+1
print(ans)


'''
1
11
111
1111
'''

for i in range(1,5):
    for j in range(1,i+1):
        print(1,end=" ")
    print()

for i in range(5,1,-1):
    for j in range(i-1):
        print(1,end=" ")
    print()

'''
1
12
123
1234
'''


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#factors
for i in range(10,50+1):
    print(i,end=" -> ")
    for x in range(1,i+1):
        if i%x==0:
            print(x,end=" ")
    print()
    

num1=int(input("enter a number"))
for x in range(2,num1):
    if num1%x==0:
        print("no it is not prime number")
        break
else:
    print("yes it is a prime number")



#Q2 Optimal method (Just for knowledge)

def factorial(n):
	ans = 1
	for i in range(2, n+1):
		ans = ans*i
	return ans

a = int(input("Lower Limit "))
b = int(input("Upper Limit "))

factorialList = []
factorialList.append(factorial(a))
for i in range(a+1,b+1):
    factorialList.append(factorialList[-1]*i)
print(factorialList)


for x in range(1,5):
    for y in range(1,x+1):
        print(1,end=" ")
    print()

for x in range(1,5):
    for y in range(1,x+1):
        print(y,end=" ")
    print()

for x in range(1,5):
    for y in range(1,6-x):
        print(y,end=" ")
    print()


for x in range(5,1,-1):                  #5 4 3 2
    for y in range(1,x):
        print(y,end=" ")
    print()
