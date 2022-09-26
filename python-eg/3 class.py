#Qs 1
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

#QS 2
x=int(input("write the base"))
y=int(input("write the exponent"))
z=x**y
print(z)

#QS 3
banana=int(input("write the no. of bananas"))
print(banana/12,"dozen")

#QS 4
days=int(input("write the no. of days"))
print("number of week is",days/7)
print("number of fortnights are",days/14)

#QS 5
xyz=int(input("write the number"))
print(xyz<<2)

#QS 6
print(4^3)
'''Its XOR operator which gives the value 
as 1 if both bits are diff and gives 
0 if both bits are same'''

#QS 7
a=int(input("write 1 no."))
b=int(input("write 2 no."))
c=int(input("write 3 no."))
print(a==b and b==c and a==c)

#QS 8
abc=int(input("Write number"))
print(not abc)
#alternate print(abc==0)