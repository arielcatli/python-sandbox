#Write a Python program to sum all the items in a list.

import random
#Generate a random list

list1 = []
for x in range(0,100):
    list1.append(random.randint(0,1))

sum = 0
for x in list1:
    sum += x


print(list1)
print(sum)