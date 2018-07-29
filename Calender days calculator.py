#normal year days and leap year days
normdays = [31,28,31,30,31,30,31,31,30,31,30,31]
leapdays = [31,29,31,30,31,30,31,31,30,31,30,31]

sw = True
while sw:
    
    #enter first date and check if correct
    print("Hello! Welcome to days calculator!!!")
    
    sw1 = True
    while sw1:
        print()
        print("Enter first date")
        y01 = int(input("Enter year:"))
        if y01>0 and (y01%4!=0 or (y01%100==0 and y01%400!=0)):
            m01 = int(input("Enter month:"))
            if 12>=m01>=1:
                d01 = int(input("Enter day:"))
                if 1<=d01<=normdays[m01-1]:
                    print()
                    print("First date is correct!!!")
                    sw1 = False
                else:
                    print()
                    print("This day does not exist")
            else:
                print()
                print("This month does not exist")
        elif y01>0:
            m01 = int(input("Enter month:"))
            if 12>=m01>=1:
                d01 = int(input("Enter day:"))
                if 1<=d01<=leapdays[m01-1]:
                    print()
                    print("First date is correct!!!")
                    sw1 = False
                else:
                    print()
                    print("This day does not exist")
            else:
                print()
                print("This month does not exist")
        else:
            print()
            print("Please enter year in A.D. only")
    
            
    #enter second date and check if correct  
    
    sw2 =True
    while sw2:
        print()
        print("Enter second date")
        y02 = int(input("Enter year:"))
        if y02>0 and (y02%4!=0 or (y02%100==0 and y02%400!=0)):
            m02 = int(input("Enter month:"))
            if 12>=m02>=1:
                d02 = int(input("Enter day:"))
                if 1<=d02<=normdays[m02-1]:
                    print()
                    print("Second date is correct!!!")
                    sw2 = False
                else:
                    print()
                    print("This day does not exist")
            else:
                print()
                print("This month does not exist")
        
        elif y02>0:
            m02 = int(input("Enter month:"))
            if 12>=m02>=1:
                d02 = int(input("Enter day:"))
                if 1<=d02<=leapdays[m02-1]:
                    print()
                    print("Second date is correct!!!")
                    sw2 = False
                else:
                    print()
                    print("This day does not exist")
            else:
                print()
                print("This month does not exist")
        else:
            print()
            print("Please enter year in A.D. only")
    
            
    
    #check if dates are in order and order them
    if y02>y01:
        [y1, m1, d1] = [y01, m01, d01]
        [y2, m2, d2] = [y02, m02, d02]
        sw = False
        
    elif y01>y02:
        [y1, m1, d1] = [y02, m02, d02]
        [y2, m2, d2] = [y01, m01, d01]
        sw = False
    
    elif y01==y02:
        if m02>m01:
            [y1, m1, d1] = [y01, m01, d01]
            [y2, m2, d2] = [y02, m02, d02]
            sw = False
        elif m01>m02:
            [y1, m1, d1] = [y02, m02, d02]
            [y2, m2, d2] = [y01, m01, d01]
            sw = False
        else:
            if d02>d01:
                [y1, m1, d1] = [y01, m01, d01]
                [y2, m2, d2] = [y02, m02, d02]
                sw = False
            elif d01>d02:
                [y1, m1, d1] = [y02, m02, d02]
                [y2, m2, d2] = [y01, m01, d01]
                sw = False
            else:   
                print()
                print("Its the same date moron")
                print("Restarting...")
                print()
            

#count days in full years in between dates full-year-days
if y2-y1>=2:
    fullyd = (365*(y2-y1-1) + (int((y2-1)/4) - int((y1+1)/4)) - (int((y2-1)/100) - int((y1+1)/100)) + (int((y2-1)/400) - int((y1+1)/400)))
else:
    fullyd = 0

#count days in first year(smaller)
if y1%4!=0 or (y1%100==0 and y1%400!=0):
    firstyd = sum(normdays[m1-1:]) - d1
    
else:
    firstyd = sum(leapdays[m1-1:]) - d1
    
#count days in second year(larger)
if y2%4!=0 or (y2%100==0 and y2%400!=0):
    secondyd = sum(normdays[:m2-1]) + d2
    
else:
    secondyd = sum(leapdays[:m2-1]) + d2
    
#total days
if y1!=y2:
    totaldays = fullyd + firstyd +secondyd
elif y1==y2 and (y2%4!=0 or (y2%100==0 and y2%400!=0)):
    totaldays = sum(normdays[m1-1:m2-1]) -d1 +d2
else:
    totaldays = sum(leapdays[m1-1:m2-1]) -d1 +d2

print()
print()
print("The number of days in between the dates are =",totaldays)
input()