import os
from time import sleep as delay

os.system('title Finding prime numbers... ')

clear = lambda : os.system('cls')
clear()
print('Importing the numbers... ')
list = open('list.txt', 'r').read()
list = list.split('\n')
last_tested = int(open('last.txt', 'r').read())
num = last_tested + 1
new = []
clear()
print('Starting... ')
delay(0.3)
clear()
tested = 0
try :
    primes_number = 0
    num = last_tested + 1
    if last_tested == 1 :
        print('2')
        print('3')
    last_found = list[-1]
    while True :
        prime = 1
        print(str(last_found))
        for i in list :
            i = int(i)
            if (num % i) == 0:
                prime = 0
                break
        if prime == 1:
            list.append(str(num))
            new.append(str(num))
            last_found = num
            primes_number += 1
        last = num
        num += 1
        tested += 1
        clear()
except KeyboardInterrupt :
    print('Saving in progress, please don\'t interrupt... ')
    open('last.txt', 'w').write(str(last))
    upload = '\n'
    if not primes_number == 0 :
        for i in new :
            if not i == new[-1] :
                upload = upload + i + '\n'
                continue
            upload = upload + i
        open('list.txt', 'a').write(upload)
    clear()
    print('Successfully saved to list.txt')
    delay(1)
    clear()
    if not primes_number == 0 :
        print('The last prime number generated is',str(new[-1])+'. ')
