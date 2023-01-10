#Q1

def isPrime(num):
    for i in range(2,num):
        if num%i == 0: 
            return 0
    return 1

def primeNumbersInRange(a,b):
    ans = []
    for i in range(a,b+1):
        prime=isPrime(i)
        if prime==1:
            ans.append(i)
    return ans

a = int(input("First num "))
b = int(input("Second num "))
print(primeNumbersInRange(a,b))



#Q2 Normal method

def factorial(n):
	ans = 1
	for i in range(2, n+1):
		ans = ans*i
	return ans

a = int(input("Lower Limit "))
b = int(input("Upper Limit "))

factorialList = []
for i in range(a,b+1):
    factorialList.append(factorial(i))
print(factorialList)



#Q3 

def createList():
    print("Enter elements of list")
    tmp = []
    for i in range(5):
        inp = input()
        tmp.append(inp)
    return tmp

l1 = createList()
l2 = createList()

l3 = []
for element in l1:
    l3.append(element)
for element in l2:
    if element not in l3:
        l3.append(element)
print(l3)