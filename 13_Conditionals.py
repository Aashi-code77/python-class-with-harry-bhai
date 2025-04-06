#  CONDITIONAL EXPRESSION 

a = int(input("Enter you age: "))

# if elif else ladder

if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("you are below the age of consent")

print(" End of program")



#  multiple if statements

a = int(input("Enter you age: "))

# if statement no:1
if(a%2 ==0):
    print("a is even")
# End of if statement no:1


# if statement no:2
if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("you are below the age of consent")

# End of if statement no:2
