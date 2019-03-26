#This statement imports the time module

import time

prefix = "th"

day = time.strftime("%d")

if day == "1" or day == "21" or day == "31":
  prefix = "st"
  day = day + prefix
elif day == "2" or day == "22":
  prefix = "nd"
  day = day + prefix
elif day == "3" or day == "23":
 prefix = "rd"
 day = day + prefix
else:
  day = day + prefix

daymonth = time.strftime("%A, %B")
year = time.strftime("%Y")
time = time.strftime("%I:""%M%p")

print(daymonth,day,year,"at",time)
