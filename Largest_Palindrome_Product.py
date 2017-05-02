#code
def largetsPalindromeProduct(n) :
    max = 0
    upperLimit = 0
    for i in range(1,(n+1)):
        upperLimit *= 10
        upperLimit += 9
        
    lowerLimit = 1+int(upperLimit/10)
    
    for i in range(lowerLimit,upperLimit+1):
        for j in range(i,upperLimit+1):
            product = i*j
            if checkPalindrome(product) :
                if product>max :
                    max = product
    return max



def checkPalindrome(number):
    digits = getDigits(number)
    length = len(digits)
    for i in range(0,int(length/2)):
        if digits[i] == digits[length-i-1]:
            continue
        else :
            return False
    
    return True
    
def getDigits(number):
    digits = []
    
    while number>0:
        digits.append(number%10)
        number = int(number/10)
    return digits

import time
start_time = time.time()
digit = int(input())
print(largetsPalindromeProduct(digit))
#print("--- %s seconds ---" % (time.time() - start_time))