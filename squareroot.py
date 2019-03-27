#Neil Moran 04/03/2019
#Solution to Q7 secondstring.py
#Taken from Ian McLoughlin video lecture on 13th March 2019

rootof = float(input("Please enter a positive number: "))
print(rootof)
est = 2

while abs((est * est) - rootof) > 0.1:
  est -= ((est * est) - rootof) / (2 * est)

round(est,2)
print(est)

print(f"The square root of {rootof} is approx. {est}.")
