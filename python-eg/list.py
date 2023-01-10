#
values=["sicsr","sig","scit"]
values.append("sibm")
print(values)

#
values=["sicsr","sig","scit"]
institutes=["ssbf","siib"]
values.append(institutes)
print(values)

#
values=["sicsr","sig","scit"]
institutes=["ssbf","siib"]
values.extend(institutes) #extends the list
print(values)

#
values=["sicsr","sig","scit"]
institutes=["ssbf","siib"]
values.extend(institutes)
values.clear()#clears all the list items
print(values)

#
values=["sicsr","sig","scit","sicsr"]
print(values.count("sicsr"))

#
values=["sicsr","sig","scit","sicsr"]
institutes=values #appends in both lists because of same memory location
institutes.append("siib")
print(institutes)
print(values)

#
values=["sicsr","sig","scit","sicsr"]
institutes=values.copy() #creates a copy and appends only in that list
institutes.append("siib")
print(institutes)
print(values)

#
values=["sicsr","sig","scit","sicsr"]
print(values.index("sicsr"))

#
values=["sicsr","sig","scit","sicsr"]
values.insert(1,"siib")
print(values)

#
values=["sicsr","sig","scit","sicsr"]
values.insert(-2,"siib") #printing before that index
print(values)

#
values=["sicsr","sig","scit","sicsr"]
print(values.pop()) #removes last element

#
values=["sicsr","sig","scit","sicsr"]
print(values.pop(1)) #removes element at 1 index

#
values=["sicsr","sig","scit","sicsr"]
del values[1:3] #removes elements from index excluding last index like slicing
print(values)

#
values=["sicsr","sig","scit","sicsr"]
values.remove("sicsr")#removes first occurence
print(values)

#
values=["sicsr","sig","scit","sicsr"]
print(len(values))

#
values=["sicsr","sig","scit","sicsr"]
values.sort()
print(values)

#
values=["sicsr","sig","scit","sicsr"]
values.sort(reverse=True) #sorts in decending order
print(values)

#
values=["sicsr","sig","scit","sicsr"]
values.reverse() #reverses the order
print(values)




