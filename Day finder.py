

normdays = [31,28,31,30,31,30,31,31,30,31,30,31]
leapdays = [31,29,31,30,31,30,31,31,30,31,30,31]

#enter date and check if correct

print()
print()
print("Hello! Welcome to day finder!!!")

sw1 = True
while sw1:
    y1 = int(input("Enter year:"))
    if y1>0 and (y1%4!=0 or (y1%100==0 and y1%400!=0)):
        m1 = int(input("Enter month:"))
        if 12>=m1>=1:
            d1 = int(input("Enter day:"))
            if 1<=d1<=normdays[m1-1]:
                sw1 = False
            else:
                print()
                print("This day does not exist")
        else:
            print()
            print("This month does not exist")
    elif y1>0:
        m1 = int(input("Enter month:"))
        if 12>=m1>=1:
            d1 = int(input("Enter day:"))
            if 1<=d1<=leapdays[m1-1]:
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
        
#find days in years before
fullyeardays = 365*(y1-1) +  int((y1-1)/4) - int((y1-1)/100) + int((y1-1)/400)

#find days in months before and days in current month - differentiate normal and leap year
if y1%4!=0 or (y1%100==0 and y1%400!=0):
    fullmonthdays = sum(normdays[:m1-1]) + d1
else:
    fullmonthdays = sum(leapdays[:m1-1]) + d1
    
#total number of days since 1st day in gregorian calender which was saturday
tdays = fullyeardays +fullmonthdays

#define week
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#find day
d = tdays%7
day = week[d-1]

print()
print("It's",day)
input()
