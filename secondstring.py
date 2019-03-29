#Neil Moran 04/03/2019
#Solution to Q6 secondstring.py

#This statement prompts the user to enter a sentance, it takes the text entered and assignes it to a string variable s
s = str(input("Please enter a sentence:"))

#s.split takes the string s and converts it to a list and names it list
list = s.split()

#The print statement takes every 2nd value that is in the list named 'list' and prints every 2nd word (or string) that is separated by a space.
#This print statement was adapted from the two URLS below
# https://towardsdatascience.com/python-basics-6-lists-and-list-manipulation-a56be62b1f95 
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row

print(*list[::2], sep=' ')
