import os
from time import sleep as delay

os.system('title Verifying prime numbers... ')

clear = lambda : os.system('cls')
clear()
print('Please enter a number to verify. ')

num = int(input())

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(str(num),"is not a prime number")
           div = num//i
           print(i,"times",str(div),"is",str(num))
           break
   else:
       print(str(num),"is a prime number")
