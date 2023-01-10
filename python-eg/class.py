value="We aRe in 307"
print(value.split(" ",2))
print(" ")

value1="                 we are in 307            "
print(value1.lstrip()+"end of string")#removes spaces from left
print(value1.rstrip()+"end of string")#removes spaces from right
print(value1.strip()+"end of string")#removes spaces from both sides
print(" ")

value2="     we are in 307........."
print(value2.strip(".").strip())
print(" ")

value3="we are in 307"
print(value3.index("307"))
#error   print(value3.index("sicsr"))
print(value3.index("e"))
print(value3.rindex("e")) #index is counting from left and search is from right
print(" ")

value4="we are in 307"
print(value4.find("307"))
print(value4.find("sicsr"))
print(value4.find("e"))
print(value4.rfind("e"))
print(" ")

value5="we are in 307"
print(value5.count("e"))
print(" ")

value6="we are in 307eeee"
print(value6.count("e",2))
print(" ")                      #includes 2 index and start finding e from 2 index

value7="we are in 307eeee"
print(value7.startswith("w"))
print(value7.startswith("e"))
print(value7.endswith("e"))
print(" ")

value8="we are in 307eeee"
print(value8.startswith("e",1,4))# checks the value bw 1 and 4 index excluding 4 index
print(value8.endswith("e",1,6))

print(value.replace("307","404"))
print(" ")


value9="we are in 307.307 is a lab"
print(value9.replace("307","408"))
print(value9.replace("307","408",1)) #checks with 1 occurence

print(value.swapcase())

value10="wearein307406"
print(value10.isalnum())#checks for spaces also  it should have only alphabets and number
print(value10.isalpha())#checks for spaces also  it should have only alphabets
print(value10.isdigit())
print(" ")

print("SICSR".isupper())
print("S IcsR".upper())
print(" ")

print("Sicsr".islower())
print("Sicsr".lower())
print(" ")

print("Sicsr Is In Pune".istitle())
print("Sicsr is in pune".istitle())
print(" ")

elements=["We","are","in","307"]
print(",".join(elements)) #work on tuple and list only not on dict

#elements=["gr","asdj",327] join should only have str
#print(" ".join(elements))   #error

print("hello"[3::-1])


