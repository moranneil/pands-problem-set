#Neil Moran 21/02/2019
#Solution to Q4 collatz.py

#Prompts the user to enter a positive integer and assigns the value to x
x = int(input("Please enter a positive integer: "))

#This while loop checks the inputed value of x to ensure it is a positive integer.
#If it isn't it prompts the user to try again.
while (x < 1):
	print("This is not a positive integer! Please try again")
	x = int(input("Please enter a positive integer: "))

while(x > 1):
  y = x % 2
  if y == 0:
    x = x // 2
    print(x)
  else: 
    x = (x * 3) + 1
    print(x)
