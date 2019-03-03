#Neil Moran 3rd March 2019
#Solution Question5 primes.py

#Prompts the user to enter a positive integer and assigns the value to x
x = int(input("Please enter a positive integer: "))

#This while loop checks the inputed value of x to ensure it is a positive integer.
#If it isn't it prompts the user to try again.
while (x < 1):
	print("This is not a positive integer! Please try again")
	x = int(input("Please enter a positive integer: "))

# y is an value that is used to divide in to the entered value x
# x is divided by the current value of y starting at 2, the remainder is added to the sum of the remainders variable
# If the sum of the remainders values is = 0 at any point then x is not a prime number
# y is increased by 1 until the value is x is reached 
y = 2

#z is the remainder variable, if z is not equal to 0 for each division until x is reached then x is a prime number
z = 0

#s is the sum variable for counting the remainder values, if s is equal to 0 when the while loop finishes then x is a prime number
s = 0

#As long as the counter y is less than the entered number x the while loop divides x by the current value of y, adds the remainder value to the remainder sum variable and checks the remainder.
#y is also incremented by 1 each time the while loop executes.
while y < x:
  z = x % y
  s = s + z
  if s == 0:
    print("This is not a prime number")
    y = x - 1
  y = y + 1
#If s is not equal to 0 after the while loop finishes then x is a prime number.
if s != 0:
  print("This is a prime")
