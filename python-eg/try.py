'''Apple="hardik"


print(Apple)

start=int(input("enter start number"))
end=int(input("enter end number"))
sum=0
count=0
for i in range(start,end+1):
    print(i) 
    sum=sum+i
    count=count+1
print(sum/count)


num=int(input("enter number"))
if num%5==0:
    print("yes it is multiple")
else:
    print("it is not")


enter1=str(input("enter the word"))
list1=[]

while enter1!="null":
    list1.append(enter1)
    enter1=str(input("enter the word"))
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)

'''

'''
for x in range(1,6):
    for y in range(5,5-x,-1):
        print(y,end=" ")
    print()


for x in range(1,5):
    for y in range(1,6-x):
        print(y,end=" ")
    print()

for x in range(1,6):
    for y in range(5,5-x,-1):
        print(y,end=" ")
    print()

'''

for x in range(1,5):
    for y in range(5,x,-1):
        print(y,end=" ")
    print()

for x in range(4,0,-1):
    for y in range(5,5-x,-1):
        print(y,end=" ")
    print()



#fibonache series
a=0
b=1
c=0
n=int(input("enter number"))
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c
print()


#factorial of range
def factorial(n):
	ans = 1
	for i in range(1, n+1):
		ans = ans*i
	return ans

a = int(input("Lower Limit "))
b = int(input("Upper Limit "))

for i in range(a,b+1):
    print(factorial(i))


#individual factorial
inp=4
s=1
for i in range(1,inp+1):
    s=s*i
print(s)


'''
arr=[]
ar=int(input("enter number of inputs"))
for i in range(1,ar+1):
    i=int(input("enter"))
    arr.append(i)
print(arr)
sum=0
for ele in range(0,len(arr)):
    sum=sum+arr[ele]
print(sum)
'''


for i in range(97,123):
    print(chr(i))

for x in range(1,5):
    for y in range(1,6-x):
        print(y,end=" ")
    print()


for x in range(1,6):
    for y in range(5,5-x,-1):
        print(y,end=" ")
    print()

no=1
for level in range(1,5):
    for step in range(1,level+1):
        print(no,end=" ")
        no=no+1
    print()

for no in range(10,1,-1):
    print(no)
    if no==5:
        break
else:
    print("hi")
                      