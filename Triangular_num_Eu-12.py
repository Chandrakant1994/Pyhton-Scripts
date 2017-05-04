# Hello World program in Python
import time
    
def num_divisors(n):
    if n % 2 == 0 : n = n/2
    divisors = 1
    count = 0
    
    while n%2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count+1)
    p = 3
    
    while n != 1:
        count = 0
        while n%p == 0:
            count+= 1
            n = n/p
        divisors = divisors * (count+1)
        p+= 2
    return divisors

def factorizationIndex(factor_limit):
    n =1 
    lnum,rnum = num_divisors(n) , num_divisors(n+1)
    
    while lnum*rnum < 500 :
        n += 1
        lnum , rnum = rnum , num_divisors(n+1)
    return n

start = time.time()
index = factorizationIndex(500)
triangle = (index * (index+1))/2
elapsed = (time.time() - start)

print("triangular number is : " + str(triangle) + " result calulated in  " + str(elapsed)+ "seconds")
