#Neil Moran 26/03/2019
#Solution to Q8 on problem set datetime.py 

#This statement imports the time module, datetime could have been imported but the program filename could not be datetime.py this caused issues with importing datetime module. The time module also had the strftime function.
import time

#This is a string variable to print by default "th" beside the day number. This is changed in the nested if statements below depending on the day of the month.
prefix = "th"

#Day is a string variable, it assigned the current day number to day
day = time.strftime("%d")
#The first if statement checks the day number to be either 1, 21 or 31, if it is any of these it assigned prefix = st, it then adds prefix on to the current day number for example 21st
if day == "1" or day == "21" or day == "31":
  prefix = "st"
  day = day + prefix
#If the day number is 2 or 22 it assignes prefix to be "nd" and "nd" is added on to either 2 or 22
elif day == "2" or day == "22":
  prefix = "nd"
  day = day + prefix
#If the day number is 3 or 23 it assignes prefix to be "rd" and "rd" is added on to either 3 or 23
elif day == "3" or day == "23":
 prefix = "rd"
 day = day + prefix
#If the day number is anything other that the numbers in the nested if statements above then the default value for "th" is added on to that string
else:
  day = day + prefix

#The format of the outputed datetime format is split in to variables using the method time.strftime and its various printed wildcard formats.
#daymonth is the first part for exampl Monday, January
daymonth = time.strftime("%A, %B")
#year is the year expressed as a 4 digit value eg 2019
year = time.strftime("%Y")
#time is the time in 12 hr format  and hr & min with a full colon and either AM or PM 
time = time.strftime("%I:""%M%p")

#The last statement is to print the above string variables in the format requested, the string variable day gives the current month day number with the correct prefix for example 1st, 2nd, 3rd or 4th etc, there is also an at inserted before the year and time variables.
print(daymonth,day,year,"at",time)
