
#FUNCTION ask for date and check if valid date and repeat question till correct date given........................
def enterdate(a):
    sw = True
    while sw:
        askdate = str(input(a))          #can be any input string-modify accordingto program (ex: a = "tell me date")
        askcorrectdate = "Enter correct date:"   #Print if wrong or invalid date
        year = int(askdate[4:])         # since input is converted to string, the dd,mm,yyyy can be-
        month = int(askdate[2:4])       #-seperated then converted to integers
        date = int(askdate[:2])
        
        normdays =[31,28,31,30,31,30,31,31,30,31,30,31]
        leapdays =[31,29,31,30,31,30,31,31,30,31,30,31]
        
        if year > 0:
            if year%4!=0 or (year%100==0 and year%400!=0): #normal years
                if 0<month<13:
                    if date<=normdays[month-1]:
                        sw = False
                        return date, month, year
                    else:
                        print(askcorrectdate)
                else:
                    print(askcorrectdate)
            elif year%4==0 or (year%100==0 and year%400==0): #leap years
                if 0<month<13:
                    if date<=leapdays[month-1]:
                        sw = False
                        return date, month, year
                    else:
                        print(askcorrectdate)
                else:
                    print(askcorrectdate)
        else:
            print(askcorrectdate)
            
            
#........................................................................................................
#FUNCTION check difference between dates(number of days in between) if given in correct order or sequence
def daysinbetween(date1,date2):
    [d1,m1,y1] = date1
    [d2,m2,y2] = date2
    
    normdays =[31,28,31,30,31,30,31,31,30,31,30,31]
    leapdays =[31,29,31,30,31,30,31,31,30,31,30,31]
    
    if (y1-y2)>=2:#count fullyears in between
        fullyeardays = (y1-y2-1)*365
        year4leapdays = int((y1-1)/4) - int((y2+1)/4)#leapyears + centuries nondivisible by 400(non leap years)
        year100leapdays = int((y1-1)/100) - int((y2+1)/100)#centuries - non leap years
        year400leapdays = int((y1-1)/400) - int((y2+1)/400)#every 400th century - leapyears
        totalfullyeardays = fullyeardays + year4leapdays - year100leapdays + year400leapdays
    else:
        totalfullyeardays = 0
    
    if (y1-y2)>=1:        
        if y1%4!=0 or (y1%100==0 and y1%400!=0): #normal years for y1
            fullmonthdays1 = sum(normdays[:m1-1])
            totalmonthdays1 = fullmonthdays1 + d1
        else:#leap years for y1
            fullmonthdays1 = sum(leapdays[:m1-1])
            totalmonthdays1 = fullmonthdays1 + d1
            
        if y2%4!=0 or (y2%100==0 and y2%400!=0): #normal years for y2
            fullmonthdays2 = sum(normdays[m2:])
            days2 = normdays[m2-1] - d2
            totalmonthdays2 = fullmonthdays2 + days2
        else:#leap years for y2
            fullmonthdays2 = sum(leapdays[m2:])
            days2 = leapdays[m2-1] - d2
            totalmonthdays2 = fullmonthdays2 + days2
            
        totaldays = totalfullyeardays + totalmonthdays1 + totalmonthdays2 # total days (full years+fullmonths

    else:#same year y1=y2
        if y1%4!=0 or (y1%100==0 and y1%400!=0): #normal years for y1 = y2
            if (m1-m2)>=1:#atleast 1 month difference
                fullmonthdays = sum(normdays[m2:m1-1])
                days1 = d1
                days2 = normdays[m2-1] - d2
                totaldays = fullmonthdays1 + days1 +days2
            elif m1==m2 and d1-d2>=1:
                totaldays = d1-d2
            else:
                totaldays = 0
                
        else: #leap years for y1 = y2
            if (m1-m2)>=1:#atleast 1 month difference
                fullmonthdays = sum(leapdays[m2:m1-1])
                days1 = d1
                days2 = leapdays[m2-1] - d2
                totaldays = fullmonthdays + days1 +days2
            elif m1==m2 and d1-d2>=1:
                totaldays = d1-d2
            else:
                totaldays = 0
    return totaldays
            
#........................................................................................................
#FUNCTION assign day names to days
def assignday(days):
    daynames = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    if days>7:
        daynumber = (days%7) - 1
    else:
        daynumber = days-1
    return daynames[daynumber]

#........................................................................................................
#ACTUAL PROGRAM
    
givedate = "Enter date(ddmmyyyy):"      #ENTER DATE
date = enterdate(givedate)              #CHECK VALIDITY OF DATE
firstdate = (1,1,1)                     #FIRST DAY OF YEAR 1 A.D.
numberofdays = daysinbetween(date,firstdate)        #FIND NUMBER OF DAYS FROM FIRST DAY(01-01-0001 A.D.)
day = assignday(numberofdays+1)         #FIND THE DAY STARTING FROM 1ST JAN 0001 WHICH WAS MONDAY

print("It's",day)



    