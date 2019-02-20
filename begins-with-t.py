#Neil Moran  
#Solution Question2 begins-with-t.py

#First the datetime is imported, this assigns the following integer value to each day of the week.
#0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday
import datetime

#The if statement determines is the current day firstly is Tue (1), then (elif) Thurs(3), if its any of these values is prints 
#Yes - today begins with a T. The 3rd option in the if statement if either statement is not true (else) prints No - today does not begin with a T. 
if datetime.datetime.today().weekday() == 1:
  print("Yes - today begins with a T.")
elif datetime.datetime.today().weekday() == 3:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")
