#Neil Moran 04/03/2019
#Solution to Q7 secondstring.py

s = str(input("Please enter a sentence:"))

list = s.split()

print(*list[::2], sep=' ')
