import math

#
num=int(input("enter a decimal number"))

def dec2bin(num):
    digit_list=[]
    while num>0:
        remainder=num%2
        digit_list.append(remainder)
        num=num//2
    print(digit_list)      
    
dec2bin(num)

#
print(abs((-10)))
print(math.ceil(9.1))
print(math.exp(10))#e value is 2.71 this statement means 2.7 raised to the power 10
print(math.floor(9.9))
print(max(1,2,3))
print(min(1,2,3))
print(pow(3,4))
print(math.pow(3,4))
print(round(2.13322,2))
print(math.sqrt(256))
print(bin(3))
print(oct(9))
print(hex(15))