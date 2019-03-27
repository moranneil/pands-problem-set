#Neil Moran  
#Solution Question2 begins-with-t.py 27/03/2019

#The time module is imported.
import time

#Day is a string variable when the function time.strftime("%w") from the time module is evaluated using the directive %w, 
# "%w" returns the weekday as a decimal number Sun(0), Mon(1), Tue(2), Wed(3), Thur(4), Fri(5), Sat(6), Sun(7). 
day= time.strftime("%w")

#The if statement evaluate the value of the string variable 'day' from the time module function time.strftime("%w"), if the value of day is either Tue(2) or Thur(4)
#it prints "Yes - today begins with a T.", if the value of 'day' is not 2 or 4 the else in the if statement prints "No - today does not begin with a T."
if day == "2" or day == "4":
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")
