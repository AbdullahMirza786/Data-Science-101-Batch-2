#14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

name=input("Enter the Name:")
rollnumber=int(input("Enter the Roll Number:"))
classheld=int(input("Enter the Number of Classes Held:"))
classeattended=int(input("Enter the Number of Classes Attended:"))

percentage=(classeattended/classheld)*100
print("NAME:",name)
print("ROLL NUMBER:",rollnumber)
print("CLASSES HELD:",classheld)
print("CLASSES ATTENDED:",classeattended)
print("Your Attendence is:",percentage)

if percentage > 75 :
    print("You are Allowed to Sit in Exam")
else:
    print("You are Not Allowed to Sit in Exam")

