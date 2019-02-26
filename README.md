# pands-problem-set
This is file documents my solutions each of the ten problems given in the pands-problem-set 2019

Question 1 sumuptp.py
This is a program that prompts for a positive integer and calculates the sum of all the number from 1 to that number, and outputs this number. The first version of the program originally took in the value enter by the user and assigned it to a string variable, the program needed another line of code to convert that string to an integer. 

The next version of this programe prompted the user for a positive integer and assigned the value to an integer variable. This required one line of code less that the previous version, there was no need to convert the string variable to an integer. 

The sumupto.py program is basically a while loop counting up and adding the sum of each of the numbers until it reaches to the entered number. This method needs three integer variables including the integer for the original number entered. 

The integer variables I used in this program are as follows:
x is the number that is entered by the user
y is used as a counter for the while loop, each time the while loop is executed the value of y is increased by 1 after the original value of y is added to z. i.e while y less than or equal to (<=) x then add the new value of y to z, 
z is the summed total of the number, the new value of y is added to this each time the while loop executes until y <= x is reached.
When y <= x exit the while loop and print z.

There is another way the same programme could be written, the counter y starts with the entered number and counts down towards and including 1 this program would have needed one less variable.




Question 2 begins-with-a-t.py
The ask here was to find out if the current day of the week began with a T. The first thing to do here was to import the days of the week using import datetime function in Python. This assigned integers to each day of the week see table below.

Function Overview:
The weekday() function of date class in datetime module, returns an integer

corresponding to the day of the week.  Here is the mapping of integer values to the days of the week.

Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6

An if and if else can ask for the two days of the week that begin with t, the final statement print if the 1st two ifs are not true

