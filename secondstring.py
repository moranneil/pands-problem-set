#Neil Moran 04/03/2019
#Solution to Q7 secondstring.py

#This statement prompts the user to enter a sentance, it takes the text entered ad assigned to the string variable s
s = str(input("Please enter a sentence:"))

#s.split takes the string s and converts it to a list and names it list
list = s.split()

#The print statement takes every 2nd value that is in the list named 'list' and prints every 2nd word (or string) that is separated by a space.
print(*list[::2], sep=' ')
