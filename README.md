 
![Alt text](/pands-problem-set/Images/Python.JPG "Python")


        
      

# Problem Set 2019

## Programming and Scripting

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
The question here is to find out if the current day of the week begins with a T. The first thing to do here was to import the days of the week using import datetime function in Python. This assigned integers to each day of the week see table below.

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

An if and if else asks for the two days of the week that begin with t, i.e Tue(1) and Thur(3), if either of these statements are true the program prints "Yes - today begins with a T.". If either of these statements are not true the last option is to print  the final statement prints "No - today does not begin with a T"

To ensure that the if statements and else if statements were working correctly I put in different print statements and different integer values so I knew what statements were been printed given a condition was true.





Question 3: divisors.py. Write a program that prints all numbers between 1,000 and 10,000 that are divisible
by 6 but not 12.

For the solution to this problem the programm uses a for loop, this for loop ran with x starting at 1000 and stopping when x was at 10000 inclusively.

In the for loop the current value of x was divided by 6 and the remainder value was assigned to y, the number x was also divided by 12 and the remainder value assigned to z.

An if statement was then used to check if x was divisible by 6 i.e y equal to 0 and x was not divisible by 12 i.e z was > 0, if this condition was true then print the current value of x.

To keep the for loop running x was incremented by 1 and it ran until x reached 10001.

The result was the program printed out all the values between 1000 and 10000 that were divisible by 6 by not by 12



