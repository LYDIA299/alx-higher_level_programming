#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastD = abs(number) % 10
if number < 0:
    lastD *= -1
str1= "Last digit of {} is {} and is {}"
if lastD > 5:
    print(str1.format(number, lastD, 'greater than 5'))
elif lastD == 0:
    print(str1.format(number, lastD, 0))
elif lastD < 6 and lastD != 0:
    print(str1.format(number, lastD, 'less than 6 and not 0'))
