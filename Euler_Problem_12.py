# Hello World program in Python
import math

def divisors(num):
    count = 2
    half = int(num/2)
    for i in range(2,half+1):
        if(num%i == 0):
            count += 1
    
    return (count)

i = 1
number = 0
while i > 0 :
    number += i
    #print(str(number) + "number of divisors : " + str(divisors(number)))
    i += 1
    noOfDivisors = divisors(number)
    if( noOfDivisors >= 500):
        print(str(number) + " number of divisors : " + str(noOfDivisors))
        break
