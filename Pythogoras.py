#Pythoras
from math import sqrt
a = float(input("Enter length of side a:"))
b = float(input("Enter length of side b:"))

c = round(sqrt(a*a + b*b), 2)

print("Length of hypotenousis:",c)