#9) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length=int(input("Enter the Length:"))
breadth=int(input("Enter the Breadth:"))
print("Length:",length)
print("Breadth:",breadth)

if length == breadth:
    print("It is Square")
else:
    print("It is Rectangle")