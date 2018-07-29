from math import *

print("Program to calculate distance and direction between positions A and B")
print()
print("Enter coordinates of position A:")
lata   = radians(float(input("Give latitude in degrees (North is positive):")))
longa  = radians(float(input("Give longitude in degrees (East is positive):")))

print()
print("Enter coordinates of position B:")
latb   = radians(float(input("Give latitude in degrees (North is positive):")))
longb  = radians(float(input("Give longitude in degrees (East is positive):")))

R = 6371.

#distance
dist = R*acos(cos(lata)*cos(latb)*cos(longb -longa) + sin(lata)*sin(latb))

#direction A to B  - eastbound A to B = alpha    -   westbound A to B = 360 -alpha
alpha = acos(cos(lata)*sin(latb) - sin(lata)*cos(latb)*cos(longb - longa))

#direction B to A
alphb = acos(cos(latb)*sin(lata) - sin(latb)*cos(lata)*cos(longa - longb))

print()
print ("Distance is {:.2f} km".format(dist))

if ((longb-longa)> 0):  #eastbound A to B AND westbound B to A
    print ("Direction from A to B = {:.2f} degrees.".format(degrees(alpha)))
    print ("Direction from B to A = {:.2f} degrees.".format((360-degrees(alphb))))
else:     #westbound A to B AND eastbound B to A
    print ("Direction from A to B = {:.2f} degrees.".format((360-degrees(alpha))))
    print ("Direction from B to A = {:.2f} degrees.".format(degrees(alphb)))
    
