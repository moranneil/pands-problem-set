#Neil Moran 28th March 2019
#Solution for Q10 plotting function x to the power of the values in the range [0,4]

#The matplotlib.pyplot is imported as plt
import matplotlib.pyplot as plt

#This is the value for x in an list
x = [0, 1, 2, 3, 4]
#This is the new list for the values of x they are calculated two to the power of x, then the values are written in to a new list twopwrx
twopwrx = []
#Y is an integer that counts through the list index
y = 0

#This for loop counts through each member of the list and calulated the 2 to the power of the current value of the list x, the for loop goes through each member of the list
for index in x[:]:
  x[y] = 2 ** x[y]
  #the new values are assigned to the new list 'twopwrx'
  twopwrx.append(x[y])
  y = y + 1

#This section plots and shows the new list 'twopwrx' , labels the x and y axis, and finally the graph of the new list 'twopwrx' 
plt.plot(twopwrx)
plt.xlabel('x = range [0-4]')
plt.ylabel('Function 2 to the power of x')
plt.show()
