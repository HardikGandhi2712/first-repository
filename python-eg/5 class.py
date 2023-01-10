#QS 1
num=int(input("input the number"))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")

#QS 2
x=input("write the sentence")
if "o" in x:
    print("o is present")
else:
    print("o is absent")

#QS 3
num1=int(input("write 1 number"))
num2=int(input("write 2 number"))
if num1>num2:
    print(num1,"is greater")
elif num2>num1:
    print(num2,"is greater")
else:
    print("Both are equal")

#QS 4
letter=input("input the letter")
list1=["a","e","i","o","u","A","E","I","O","U"]
if letter in list1:
    print(letter,"is vowel")
else:
    print(letter,"is not a vowel")

#Qs 5
num1=int(input("write 1 number"))
num2=int(input("write 2 number"))
for x in range(num1,num2+1):
    if (x%2==0):
        print(x)

#QS 6
list1=[32,23,45,56,21]
for x in list1:
    print(x**2)