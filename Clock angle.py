
h = int(input("Enter Hour:"))
m = int(input("Enter Min:"))

if 0<=h<=23 and 0<=m<=59:
    if h<=12:
        angh = (360*h/12) + (360*m)/(12*60)
        angm = 360*m/60
        
    else:
        angh = (360*(h-12)/12) + (360*m)/(12*60)
        angm = 360*m/60
        
    ang = round(abs(angh-angm))
    if ang<180:
        print( "Angle is:",ang,"degrees")
    else:
        ang = 360. - ang
        print( "Angle is:",ang,"degrees")
        
else:
    print("Enter valid numbers")
input()
    
    

