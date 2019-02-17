#Neil Moran  
#Solution 1 

#The number is taken in as a string
xString = input("Enter a positive integer: ")

#This line converts the string variable to an integer
x = int(xString)

# y is an integer variable for the counter in the while loop
y = 0

#z is an integer variable for the calculated value
z = 0

while y <= x:
    z = z + y
    y = y + 1

print(z)
