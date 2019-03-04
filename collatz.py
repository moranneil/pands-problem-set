#Neil Moran 21/02/2019
#Solution to Q4 collatz.py

#Prompts the user to enter a positive integer and assigns the value to x
x = int(input("Please enter a positive integer: "))

#n is a list to print all the calculated values out on one line.
n = []

#This while loop checks the inputed value of x to ensure it is a positive integer.
#If it isn't it prompts the user to try again.
while (x < 1):
	print("This is not a positive integer! Please try again")
	x = int(input("Please enter a positive integer: "))

#While loop to determine if the number is even or odd by dividing by 2 an checking the remainder y, depending on the result the if statement divides by 2 or multiplies by 3 and adds 1.
#Along with the mathematical function each if statement appends the new value of x to the same list n.
#While loop terminates when x > 1 this allows the while loop to execute until x finally is 1 then it stops.
while(x > 1):
  y = x % 2
  if y == 0:
    x = x // 2
    n.append(x)
  else: 
    x = (x * 3) + 1
    n.append(x)

#prints the list n without square brackets and commas between the values & inserts a space between the integers in the list
print(*n, sep=' ')
