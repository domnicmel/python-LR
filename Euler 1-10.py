#2
f =1
s =2
tot = s
lst=[f,s]
while s+f<4000000:  
    s = s+f
    f = s-f
    lst.append(s)
    if s%2==0:
        tot = tot+s  
print(tot)


#............................................................................................................................
#3 - prime factorisation
s = 317584931803


quo =[]                 #add quotients to the list 
pri = []                #add prime divsior to list or prime factors)
i =0
while i in range(s):     
    i =i+1
    if i>=2 and s%i==0:         #if s is divisible by a number
        pri.append(i)           #add the number to pri since it is a divisor
        while s%i==0:           #and check if s is divisible by the number any more times
            j = int(s/i)        
            quo.append(j)       #add the quotient to list, everytime it is divisible by a divisor, even if its the same divisor
            s = int(s/i)        #every time it is divisible by a divisor, s is updated to be the new quotient
                                #loop continues till all numbers in s have been checked
                                #s keeps getting smaller, as quotiens are found and divisors are added to list
                                # since all divisors are used till the new s is no longer divisible by them,- 
                                #-all multiples of prime numbers are not added to pri list,-
                                #-therefore adding only prime numbers to the list
                                
                                #NOTE - I am not sure how to skip even numbers and multiples of prime numbers in the loop.
print("the highest prime factor is" ,max(pri)) 


#new version improved
import time
import math

start = time.time()
s = 317584931803333

quo =[]                 #add quotients to the list 
pri = []                #add prime divsior to list or prime factors)
i =2
     
if s%i==0:
    pri.append(i)
    while s%i==0:           
        j = (s/i)        
        quo.append(j)       
        s = int(s/i)

i = i+1

while i <= math.sqrt(s+1):
    
    while s%i==0:
        pri.append(i)                 
        j = int(s/i)        
        quo.append(j)      
        s = int(s/i)
    i = i+2
    
if(s > 1):
    pri.append(s)
                
print("the highest prime factor is" ,max(pri)) 
print(time.time()-start)





#.............................................................................................................................
#4 - palindrome
i =99   #min 3 digit number-1

lgnum = 0   #largest so far!!
lst1 =[]    #add first 3 digit num to list, multiple of which is a palindrome
lst2 =[]    #add pair of first 3 digit num, both these multiply to goive palindrome
lst3 =[]    #adds palindrome to list

while i<1000:       #loops till i<1000
    i = i+1         #starts with i = 100, smallest 3 digit number
    j =i            #starts with same number for j
    while j<1000:   # for every j from 100 till 1000, checks multiple for current i
        num = str(int(j*i))     #converts the multiple to string 
        if num == num[::-1]:    #checks if string(number stored as string) is same if reversed (palindrome)
            lst1.append(i)      #if palindrome adds i to list
            lst2.append(j)      #adds j to list 
            lst3.append(int(num))           #adds palindrome number to list                
        j = j+1                             #increases j by 1 for next loop
                                            #therefore for every i, it checks j from i to 999,-
                                            #-so that same p0air of numbers is not checked again
                                            #can be done from i=j=999 and backwards also!!!
print("highest palindrome is", max(lst3))



#............................................................................................................................
#5 - smallest multiple
#my method - Takes long and too many useless iterations
n = int(input("Enter number:"))
sw = True
a = list(range(1,n+1))

b = n
while sw:
    b+=n
    sw = not all(b%i==0 for i in a)
print("Smallest number divisible by all numbers below",n,"is",b)
#can be done better - approach is wrong -increasing numbers by n and checking if divisible by all............................

# found online methid based - multipley along number by number till the final number each stp is -
#-divisible by all previous numbers in n
i = 1

for k in (range(1, 21)):
    if i % k > 0:

    
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print (i)
# better method and works for larger numbers




#...........................................................................................................................
#6 difference of sum of squares and squares of sum

a = int(input("Enter number:"))

b = list(range(1,a+1))
c = []

for i in range(a):
    d = b[i]*b[i]
    c.append(d)
e = sum(c)
f = sum(b)*sum(b)
g = abs(e-f)

print()
print("Sum of squares is",e)
print("Squares of sum is",f)
print("Difference between sum of squares and squares of sum is",g)
#..........................................................................................................................

#7
from math import sqrt
l =[2]
a =3
sw =True
while sw:
    for i in l:
        if len(l)==10001:
            sw =False
        elif i<=int(sqrt(a)+1) and a%i==0:
            a=a+2
        elif all(a%i!=0 for i in l) :
            l.append(a)
            a=a+2

print(l[-1])
        
#............................................................................................................................