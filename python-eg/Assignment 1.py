
#Qs1)
num=input("Enter a number ")
Digits=list(num)
Sum=int(Digits[0])**3+int(Digits[1])**3+int(Digits[2])**3
if int(num)==Sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")


#Qs2)
nationality=input("Enter your nationality ")
if nationality=="India":
    state=input("Enter your state ")
    if state=="Pune":
        print("You are on the waitlist for hostel accomodation")
    else:
        print("You are eligible for hostel accomodation")
else:
    print("Please visit the International office")
