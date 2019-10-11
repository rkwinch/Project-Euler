'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt

def otherFactor(num1, num2):
  num3 = num1 / num2
  return num3

def isPrime(val):
  flag = True
  for j in range(2, int(sqrt(val))):
      if val % j == 0 and val != j:
        flag = False
  if flag == True:
    return True
  else:
    return False
    
x = 600851475143
maxPrime = 0
potMaxPrime = 0
squareRootInt = int(sqrt(x))

for i in range(2, squareRootInt):
  if x % i == 0:
    if isPrime(i) == True:
      prime1 = i
      potMaxPrime = prime1
      potentialOtherFactor = otherFactor(x, i)
      if isPrime(potentialOtherFactor) == True:
        prime2 = potentialOtherFactor
        potMaxPrime = prime2 
  maxPrime = potMaxPrime if potMaxPrime > maxPrime else maxPrime
print maxPrime
