#QS 1)
string=input("enter the value of string")
str=""
for x in string:
    str=x+str
print("reversed string",str)


#Qs 2
string1=input("enter the value")
count1=0
count2=0
for i in string:
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count2=count2+1
print("number of lowercase letters",count1)
print("number of uppercase letters",count2)
print()

#Qs 3
string2=input("enter 1 value")
string3=input("enter 2 value")
a=string2+" "+string3
print(a)
print()

#Qs 4
str1=input("enter the value of string")
length=len(str1)
if length>=3:
    if str1.find("ing"):
        print(str1.replace("ing","ly"))
    print(str1+"ing")
elif length<3:
    print(str1)
print()

#Qs 5
str2=input("enter")
b="poor"
if b in str2:
    print(str2.replace("poor","good"))


