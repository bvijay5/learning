age = int(input("Enter your age: "))

if(age>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(age<0):
    print("Invalid input!")

else:
    print("You are below the age of consent")

print("End of program")