#15) Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

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
medicalcause=input("Enter your Medical Cause:")
if percentage > 75 :
     if medicalcause =='Y' or 'y':
        print("You are Allowed to Sit in Exam")
else:
    print("You are Not Allowed to Sit in Exam")


