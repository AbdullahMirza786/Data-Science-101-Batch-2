#1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
salary=int(input("Enter the Salary:"))
yearofservice=int(input("Enter the Year of Service:"))
print("Salary:", salary)
print("Year of Service:", yearofservice)

if yearofservice > 5:
    print("Congratulations! You've just received a 5% bonus added to your salary!\n", 500 (salary*0.05))
else:
    print("Your Regular Salary has been Deposited:",salary)


