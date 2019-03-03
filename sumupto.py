#Neil Moran  
#Solution Question1 sumupto.py 

#Prompts the user to enter a positive integer and assigns the value to x
x = int(input("Please enter a positive integer: "))

#This while loop checks the inputed value of x to ensure it is a positive integer.
#If it isn't it prompts the user to try again.
while (x < 1):
	print("This is not a positive integer! Please try again")
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
