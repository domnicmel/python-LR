#Interest

a = float(input("Enter principal amount:"))
r = float(input("Enter rate of interest:"))
y = float(input("Enter number of years:"))

A = a*(1+ r/100)**y

print()
print("The End amount is: {:.2f}".format(A))