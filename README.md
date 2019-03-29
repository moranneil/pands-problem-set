 
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





## Question3: divisors.py

This program prints all numbers between 1,000 and 10,000 that are divisible
by 6 but not 12.

The solution to this problem the program uses a for loop, this for loop runs with x starting at 1000 and stopping when x was at 10000 inclusively, 10001 had to be coded in the for loop range. See image of the for loop below

![For Loop](Images/divisors-for-loop.JPG "For Loop")

In the for loop the current value of x was divided by 6 and the remainder value was assigned to y, the number x was also divided by 12 and the remainder value assigned to z. y and z are given initial values of 0 before the for loop is executed.

An if statement nested within the for loop was then used to evaluate if the current value of y was equal to 0 and z was not equal to 0, if both conditions were true then the current value of x is divisible by 6 and not divisible by 12, the current value is x is printed to the screen.  

To keep the for loop running x was incremented by 1 and it ran until x reached 10000.

The result was the program printed (on a new line) out all the values of x between 1000 and 10000 that were divisible by 6 by not by 12.


## Question4: collatz.py

This program prompts the user to input any positive integer, then it outputs successive values of the following calculation, if the current value was even divide it by 2 and if it was odd multiply it by three and add one. THe program runs until the value of x reaches 1.

The first task in this program was to prompt the user, take in the value entered and check it its a positive number.

The while loop below checks if the value is a postive number, this is assigned to the integer variable x.

![Positive Number Check](Images/collatz-positive-number-check.JPG "Number Check")

Once the positive integer is passed in by the user the while loop below is executed, the while loop divides the current value of x and determines if the integer is odd or even, by assigning the value of the remainder of the division to the variable y.  

![While Loop](Images/collatz-while-loop.JPG "While Loop")

The variable y is evaluated in an if statement within the while loop and depending on if y == 0 (even) x is divided by two or (else) x is odd and is multiplied by 3 and 1 is added. The resulting new value for x is then appended to a list 'n' each time whether its even or odd. This creates a list n with all the values of x until the while loop stops running when x reaches 1.

The resulting list n is printed out without the square brackets and the values are separate by a space this is achieved by using the print command below.

![Print List](Images/collatz-print-list.JPG "Print List")

## Question 5: primes.py

This program prompts the user to input a positive integer and tells the user if its a prime number.

Like the other programs the user is prompted for a positive integer and the while loop checks if the number is positive. It re prompts the user if it is not a positive number.

![Positive Number Check](Images/primes-positive-integer-check.JPG "Positive Number Check")

The two cases for 1 and 2 are given as printed statements below

![1 & 2](Images/primes-1-and-2.JPG "1 & 2")

The while loop determines if the number entered is a prime number by dividing the number x by a number y and assigning it to the variable z see line 32, y = 2 at the beginning.  Each time this division occurs in the while loop the if statement checks the value of the remainder z see line 33, if z is 0 after any division then the number is not a prime number and "This is not a prime number" is printed to the screen. There is a break statement in the if statement on line 35, this breaks out of the while loop after the "This is not a prime number" is printed. y is incremented by 1 every time the while loop executes and the if statement evaluation is false see line 37.

![Primes While Loop](Images/primes-while-loop.JPG "Primes While Loop")

If z is not equal to 0 after every successive division then the number is a prime number, the while loop exits when y is no longer less that x as mentioned, it is incremented by 1 every time the while loop executes.

Once the while loop finishes the if statement at the end checks the value of z if its not = 0 then the number is a prime number and "This is a prime" is printed to the screen.

## Question 6: secondstring.py

This program takes a users input string and prints out every second word. This program 


![Secondstring Sting Input](Images/secondstring-string-input.JPG "Secondstring Sting Input")

![Secondstring Convert String to List](Images/secondstring-convert-string-to-list.JPG "Secondstring Convert String to List")

![Secondstring Print](Images/secondstring-convert-prints-every-2nd-word-on-the-list-without-brackets.JPG "Secondstring Print")

## Question 7: squareroot.py

This program takes a positive floating point number from the user and outputs its square root approximation.

## Question 8: datetime.py

This program outputs todays days in the format Monday, January 10th 2019 at 1:15pm

## Question 9: second.py

This program takes a file name given as an argument and outputs every 2nd line to the screen.

## Question 10: plots.py

These programs plot the function x, x<sup>2</sup>, 2<sup>x</sup> for the values of x been in the range [0-4]
