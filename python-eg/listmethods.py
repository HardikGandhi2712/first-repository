string=str(input("enter"))
for letters in set(string):
    if string.count(letters)>1:
        print(letters,end=" ")
print("")


str1=(input("enter a string"))
list2=[]
for words in str1:
    if (words.count):
      list2.append(words.count)
print(list2)

#Qs2)
para=(input("enter the paragraph"))
word=(input("enter the word"))
for x in para:
    para.replace(word," ")
print(para)


#Qs3)
values=set()
for i in range (1,6):
    data=input("enter a value")
    values.add(data)
print(values)

#Qs 4
values1=dict()
values1["prn1"]="jane"
values1["prn2"]="mane"
values1["prn3"]="kane"
values1["prn4"]="insane"

prn=input("enter prn")
name=input("enter name")
values1[prn]=name

print(values1)

#Qs5
for key,value in values.items:
    print(key,value)
