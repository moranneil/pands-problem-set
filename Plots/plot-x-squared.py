#Neil Moran 28th March 2019
#Solution for Q10 plotting function x squared is in the range [0,4]

#The matplotlib.pyplot is imported as plt
import matplotlib.pyplot as plt

#This is the value for x in an list
x = [0, 1, 2, 3, 4]
#This is the new list for the squared values of x written in to a new list twopwrx
xsqr = []
y = 0

for index in x[:]:
  x[y] = x[y] * x[y]
  xsqr.append(x[y])
  y = y + 1
print(xsqr)
plt.plot(xsqr)
plt.xlabel('x = range [0-4]')
plt.ylabel('Function x squared')
plt.show()
