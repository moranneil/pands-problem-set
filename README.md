 
![Python](Images/Python.JPG "Python")


        
      

# Problem Set 2019

## Programming and Scripting

This is file documents my solutions each of the ten problems given in the Programming and Scripting Problem Set 2019


## Question1 sumupto.py

This is a program that prompts for a positive integer and calculates the sum of all the number from 1 to that number, and outputs this number. The program also checks the inputed value to ensure its a positive number using a while loop and if is not it reprompts the user

![Positive Number Check](Images/sumupto-positive-number-check.JPG "Number Check")

The sumupto.py program is a while loop counting up and adding the sum of each of the numbers until it reaches to the entered number. This method needs three integer variables including the integer for the original number entered. 

![While Loop](Images/sumupto-while-loop.JPG "While Loop")

The integer variables I used in this program are as follows:
x is the number that is entered by the user
y is used as a counter for the while loop, each time the while loop is executed the value of y is increased by 1 after the original value of y is added to z. i.e while y less than or equal to (<=) x then add the new value of y to z, 
z is the summed total of the number, the new value of y is added to this each time the while loop executes until y <= x is reached.
When y <= x exit the while loop and print z.

There is another way the same programme could be written, the counter y starts with the entered number and counts down towards and including 1 this program would have needed one less variable.




## Question2 begins-with-a-t.py
This program checks if the current day of the week begins with a T. The first working version of this program imported the module 'datetime', this however stopped working when the program for Question 8 was written as the filename datetime.py was specified in the question, once datetime.py was in the same folder as begins-with-a-t.py it caused a problem with importing the module library from the correct source. 

To overcome this, the module 'time' was imported instead. The program uses the function 'time.strftime' with the directive %w, this directive assigns a decmial number to each day of the week see below. 

Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6

The variable 'day' is assigned this decimal number, this is a string variable.

![Time Function](Images/begins-with-a-T-time.strtime.JPG "Time function")

If statements are used to check is the variable 'day' either 2 or 4, if it is then the current day is Tuesday or Thursday and "Yes - today begins with a T." is printed to the screen. The else in the if statement is used when the first if statement is evaluated to false and "No - today does not begin with a T." is printed to the screen.

![If Statement](Images/begins-with-a-T-if-statement.JPG "If Statement")





## Question 3: divisors.py. 

This program prints all numbers between 1,000 and 10,000 that are divisible
by 6 but not 12.

The solution to this problem the program uses a for loop, this for loop runs with x starting at 1000 and stopping when x was at 10000 inclusively, 10001 had to be coded in the for loop range.

![For Loop](Images/divisors-for-loop.JPG "For Loop")

In the for loop the current value of x was divided by 6 and the remainder value was assigned to y, the number x was also divided by 12 and the remainder value assigned to z.

An if statement within the for loop was then used to evaluate if the current value of y was equal to 0 and z was not equal to 0, if both conditions were true then the current value of x is divisible by 6 and not divisible by 12, the current value is x is printed to the screen.  

To keep the for loop running x was incremented by 1 and it ran until x reached 10000.

The result was the program printed (on a new line) out all the values of x between 1000 and 10000 that were divisible by 6 by not by 12.



