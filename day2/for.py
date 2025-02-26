# for loop = it repeats the block of code at the exact amount of times


for i in range(10):
    print(i)
for i in range(1, 11):
    print(i)
for i in range(1, 11, 2):
    print(i)

name = input("Enter Your Name: ")
for letter in name:
    print(letter)

name = input("Enter Your Name: ")
for letter in name:
    print(letter, end=" ")

import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("RAMADAN MUBARAK !")
