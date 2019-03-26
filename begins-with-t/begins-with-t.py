#Neil Moran  
#Solution Question2 begins-with-t.py

#The datetime module is imported.

import datetime

#The nested if statments evaluate the value of datetime.datetime.today().weekday() from the datetime module that was imported in line 6. The possible values are
#Mon(0), Tue(1), Wed(2), Thur(3), Fri(4), Sat(5), Sun(6)
#The if statement determines is the current day firstly is Tue (1), then (elif) Thurs(3), if its any of these values it prints "Yes - today begins with a T."
#The 3rd option in the if statement if either of the 1st two statements are not true, it then (else) prints "No - today does not begin with a T."
if datetime.datetime.today().weekday() == 1:
  print("Yes - today begins with a T.")
elif datetime.datetime.today().weekday() == 3:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")
