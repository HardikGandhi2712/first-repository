#strings are immutable
value="SICSR is located in Pune"
print(value.upper()) #uppercase all the letters
print(value.lower()) #lowercase all letters

print(value.capitalize()) #first letter capital of entire string rest all small
print(value.title()) #first letter of every word becomes capital
print(len(value)) #number of characters including spaces 


#ascii value  A=65  a=97

print(ord("a")) #it gives ascii value letter to ascii
print(chr(97)) #opposite of ord returns letter

print(value[1:4]) #extracting value not including ending index slice function
print(value[:]) #gives entire value
print(value[::2]) #print whole but after every 2 steps just like go to every second letter
print(value[:2:]) #value till 2 but 2 is not included so 0 and 1 value will be displayed
print(value[2:]) #skipping first 2 letters
print(value[::-1]) #reverses the string 
print(value[::-2]) #reverses and step of 2
print(value[-1]) #last character
print(value[:-1]) #leave the last character
print(value[-2:-4:-1])
print(value[-4:-2:-1])#empty value