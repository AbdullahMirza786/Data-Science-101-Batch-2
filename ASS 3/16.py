#13) Take input of age of 3 people by user and determine oldest and youngest among them.
a=int(input("Enter the Age:"))
b=int(input("Enter the Age:"))
c=int(input("Enter the Age:"))
print("PERSON 1:",a)
print("PERSON 2:",b)
print("PERSON 3:",c)

if a > b and a > c:
    print("PERSON 1 is Highest:",a)
elif b > a and b > c:
    print("PERSON 2 is Highest:",b)
else:
    print("PERSON 3 is Highest:",c)
