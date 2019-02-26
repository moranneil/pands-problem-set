#Neil Moran  
#Solution Question1 sumupto.py 

x = int(input("Please enter a positive integer: "))

# y is an integer variable for the counter in the while loop
y = 0

#z is an integer variable for the calculated value
z = 0

#As long as the counter y is less than or equal to the entered number x the while loop adds the next number to the sum until the number given x is reached
# y is also incremented by 1 each time the while loop executes
while y <= x:
    z = z + y
    y = y + 1

#When y greater that x exit the while loop and print the summed total z

print(z)
