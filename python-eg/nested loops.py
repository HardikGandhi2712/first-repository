# QS 1
num=int(input("enter a number"))
sum_dig=0
while(num!=0):
    last_digit=num%10
    sum_dig=sum_dig+last_digit
    num=num//10
print(sum_dig)   


#QS 2 a
i=5
while i<10:
    print(i)
    i=i+1
else:
    print("inside else")

'''The output for this is 5 6 7 8 9 this happens because first the starting value was 5 and it then goes to while loop which says i<10 so it will first print
 i which is 5 and then by incrementation it increased the value by 1 and now the value for i is 6 it will keep on going until it is 9 and ends when it becomes
10 because there is no equality operator and then print the else statement'''

#b
i=5
while i<10:
    print(i)
    i=i+1
    break
else:
    print("inside else")

'''The output for this is only 5 because the value of i was less than 10 so it will go in while loop and then it will print the value 5 after that it will
increment the value but because of break it will break the while loop'''


#Qs 3
num1=int(input("enter the base number"))
num2=int(input("enter the value of power"))
power=1
for i in range(1,num2+1):
    power=power*num1
print(power)
