'''
A Palindromic number reads the same both ways.  The largest palindrome made
from the product of two 2-digit numbers is 91 * 99 = 9009.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

maxNum = 0

def isPalindrome(val):
  flag = False
  google=[]
  val = str(val)
  for i in range(len(val)-1,-1,-1):
    google.append(val[i])
  google = ''.join(google)
  google = int(google)
  if int(val) == google and int(val) > 10000: #100*100 = 10000 which is smallest product possible
    flag = True                                #from the smallest three digit numbers
  return True if flag == True else False

def maxNumber(product,maxNum):
  if product > maxNum:
    return product
  else:
    return maxNum
    

for i in range(999,0,-1):
  for j in range(999,0,-1):
    product = i * j
    if isPalindrome(product)==True:
      maxNum=maxNumber(product,maxNum)
      break

print maxNum
