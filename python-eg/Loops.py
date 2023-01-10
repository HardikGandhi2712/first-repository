#QS1)
num1=int(input("write 1 number"))
num2=int(input("write 2 number"))
for x in range(num1,num2+1):
    if (x%2==0):
        print(x)

#QS 2)
number=int(input("Write the number you want the table of"))
table=int(input("Write the number till you want the table"))
for i in range(1,table+1):
    print(number,"*",i,"=",number*i)


#Qs 3)
list=[32,23,45,56,21]
for x in list:
    print(x**2)

list=[32,23,45,56,21]
for x in range(0,len(list)):
    print(list[x]**2)
    


