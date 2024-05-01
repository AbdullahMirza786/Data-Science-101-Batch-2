#17) Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and 
#then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR"

age=int(input("Enter the age:"))
gender=(input("Enter the Gender(M or F):"))
maritalstatus=(input("Enter the Marital Status(Y or N):"))
print("AGE:",age)
print("GENDER:",gender)
print("MARITAL STATUS:",maritalstatus)
if gender == 'F' :
    print("she will work only in urban areas")
elif gender == 'M' and ( age >= 20 and age <40) :
    print("he may work in anywhere")
elif gender =='M' and  ( age >= 40 and age <60) :
    print("he will work in urban areas only")
elif age < 20 :
    print("ERROR")


