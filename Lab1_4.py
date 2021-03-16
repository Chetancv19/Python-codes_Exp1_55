#Chetan Velonde 3019155
#Python Program to Generate a Random Number
import random
a = int(input("The start of the range: "))
b = int(input("The end of the range: "))

c = random.randint(a, b+1)
print("Random number generated: "+str(c))