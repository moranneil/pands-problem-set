#Neil Moran 28th March 2019
#Solution for Q10 plotting function x squared is in the range [0,4]

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
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
