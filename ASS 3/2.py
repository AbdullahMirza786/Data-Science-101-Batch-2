#2) Write a program to check whether a person is eligible for voting or not. 
#(accept age from user) if age is greater than 17 eligible otherwise not eligible

age=int(input("Enter the Age:"))
print("AGE:",age)
if age > 17:
     print("You are Eligible for Voting ")
else:
    print("You are not Eligible for Voting")