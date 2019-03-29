#Neil Moran 04/03/2019
#Solution to Q7 squareroot.py
#Taken from Ian McLoughlin video lecture on 13th March 2019

rootof = float(input("Please enter a positive number: "))

#This while loop checks the inputed value of 'rootof' to ensure it is a positive number.
#If it isn't it prompts the user to try again.
while (rootof < 0.1):
  print("This is not a positive number! Please try again")
  rootof = float(input("Please enter a positive number: "))

#This is the guess of the estimated value of the square root of the number  
est = 2
#The while loop runs when the absolute value of the (est squared) - (the given number 'rootof') and checks its greater that 0.1, if a more accurate approximation is needed then 0.1 needs to be smaller eg .001
while abs((est * est) - rootof) > 0.1:
  #((est squared) - rootof))/(2 * est) is subtracted from est, this is repeated until  the while loop evaluation above is false
  est -= ((est * est) - rootof) / (2 * est)
#This variable 'roundest' rounds the variable number 'est' to be one decimal place
roundest = round(est,1)
#Prints the original value and the rounded answer to the screen
print(f"The square root of {rootof} is approx. {roundest}.")
