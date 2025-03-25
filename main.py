# Name: Akindu Ariyratna
# Title: 
# Date: March 19th 2025
# Description: This program prints 100 numbers and finds the average

import random 
Numbers = []

for i in range(1,100):
    number = random.randint(0,100)
    print(number)
    Numbers.append(number)

print(sum(Numbers)/100)

