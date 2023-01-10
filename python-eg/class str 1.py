#Qs 1
str1=str(input("enter 1 string"))
str2=str(input("enter 2 string"))
x=sorted(str1)
y=sorted(str2)
if x == y:
    print("they form anagrams")
elif str1 != str2:
    print("they dont form anagrams")


#Qs2
string=str(input("enter"))
for letters in set(string):
    if string.count(letters)>1:
        print(letters,end=" ")
print("")


#Qs3
str3=str(input("enter the value of string"))
d=dict()

for letter in set(str3):
    d[letter]=str3.count(letter)

value=max(d.values())
for char in d:
    if d[char]==value:
        print(char)

#
value=input("enter the string")
max_count=0
max_letter=""

for letter in value:
    if letter!=" " and value.count(letter)>max_count:
        max_count=value.count(letter)
        max_letter=letter
        print(max_letter)


#Qs4
email=str(input("enter the email"))

def emailisvalid(email):
    idx=email.rfind('.')
    if idx==-1:
        return False
    for i in range(idx+1,len(email)):
        if email[i].isdigit():
            return False
    return True


if not email=='' and email.count('@')==1 and (not email.startswith("@")) and (not email.endswith("@")) \
and (not email.startswith(".")) and (not email.endswith(".")) and (not email[0].isdigit()) and emailisvalid(email):
    print("yes it is valid")
else:
    print("email is not valid")



