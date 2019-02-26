#Neil Moran  
#Solution Question3 divisors.py

#These variables y and z are needed to determine if the current number (x) is divisible by 6 (y) and 12 (z)
y = 0 
z = 0

# This is a for loop that takes the value x and counts from 1000 up to and including 10000.
# If x is in the configured range from 1000 - 10000 inclusively, it divides x by 6 and assigns the remainder value to y, it also divides the same value of x by 12 and assigns the remainder value to z
# The if statement checks the number was divisible by 6 i.e the remainder (y) is equal to 0 and also if z > 0 i.e the number is not divisible by 12.
# If this statement is true print the current value of x, then increase x by 1 and perform the same for loop again whle the value of x is in the range 1000 - 10000 inclusively.
# The results prints out all the number between 1000 - 10000 that are divisible by 6 but not divisible by 12 
for x in range(1000, 10001):
  y = x % 6
  z = x % 12
  if y == 0 and z > 0:
    print(x)
  x = x + 1
