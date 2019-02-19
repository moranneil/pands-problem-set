#Neil Moran  
#Solution Question2 begins-with-t.py

#First the datetime is imported
 
import datetime

if datetime.datetime.today().weekday() == 1:
  print("Yes - today begins with a T.")
elif datetime.datetime.today().weekday() == 3:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")
