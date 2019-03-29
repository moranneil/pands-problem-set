#Neil Moran 3rd March 2019, modified on 29th March 
#Solution Question5 primes.py

#Prompts the user to enter a positive integer and assigns the value to x
x = int(input("Please enter a positive integer: "))

#This while loop checks the inputed value of x to ensure it is a positive integer.
#If it isn't it prompts the user to try again.
while (x < 1):
	print("This is not a positive integer! Please try again")
	x = int(input("Please enter a positive integer: "))

#This is stating that 1 is not a prime number if entered
if x == 1:
  print("This is not a prime number")

#This is stating that 2 is a prime number if entered as the while loop won't run if x = 2
if x == 2:
  print("This is a prime")


# x is divided by the current value of y starting at 2.
# y is a value that is used to divide in to the entered value x
y = 2

#z is the remainder variable, if z is not equal to 0 for each division until x is reached then x is a prime number
z = 0

#As long as the counter y is less than the entered number x the while loop divides x by the current value of y, adds the remainder value to the remainder sum variable and checks the remainder.
#y is also incremented by 1 each time the while loop executes.
while y < x:
  z = x % y
  if z == 0:
    print("This is not a prime number")
    break
    #break is use here to stop the while loop if z = 0, the number x is not a prime number. 
  y = y + 1
  # y is increased by 1 until the value of x is reached

#If z is not equal to 0 after the while loop finishes then x is a prime number.
if z != 0:
  print("This is a prime")


  
