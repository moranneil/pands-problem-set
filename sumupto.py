#Neil Moran  
#Solution Question1 sumupto.py 

x = int(input("Please enter a positive integer: "))

# y is an integer variable for the counter in the while loop
y = 0

#z is an integer variable for the calculated value
z = 0

#As long as the counter y is less that or equal the while loop adds the next number to the sum until the number given is reached
while y <= x:
    z = z + y
    y = y + 1

#Prints the calculated value
print(z)
