#Neil Moran 21/02/2019
#Solution to Q4 collatz.py

x = int(input("Please enter a positive integer: "))

while(x > 1):
  y = x % 2
  if y == 0:
    x = x / 2
    print(x)
  else: 
    x = (x * 3) + 1
    print(x)
