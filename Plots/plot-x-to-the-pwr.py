#Neil Moran 28th March 2019
#Solution for Q10 plotting function x to the power of the values in the range [0,4]

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
twopwrx = []
y = 0

#print(x[y])

for index2 in x[:]:
  x[y] = 2 ** x[y]
  twopwrx.append(x[y])
  y = y + 1

print(twopwrx)

plt.plot(twopwrx)
plt.xlabel('x = range [0-4]')
plt.ylabel('Function x to the power')
plt.show()
