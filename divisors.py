#Neil Moran  
#Solution Question3 divisors.py


y = 0 
z = 0


for x in range(1000, 10001):
  y = x % 6
  z = x % 12
  if y == 0 and z > 0:
    print(x)
  x = x + 1
