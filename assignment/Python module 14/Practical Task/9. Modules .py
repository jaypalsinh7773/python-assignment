#1->Write a Python program to import the math module and use functions like sqrt(), ceil(), 
#floor(). 

# import math

# num = 15.7

# square = math.sqrt(num)
# ceiling = math.ceil(num)
# floor = math.floor(num)

# print("Square Root:", square)
# print("Ceil Value:", ceiling)
# print("Floor Value:", floor)


#2-> Write a Python program to generate random numbers using the random module.

import random

rand_int = random.randint(1, 100)
rand_float = random.random()
rand_choice = random.choice([10, 20, 30, 40, 50]) 

print("Integer:", rand_int)
print("Float:", rand_float)
print("Choice:", rand_choice)