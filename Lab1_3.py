#Chetan Velonde 3019155
#Python Program to Swap Two Variables

print("Enter two number to swap:")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before Swap:\n")
print("a = " + str(a) + " and b = " + str(b) + "\n")

temp = a
a = b
b = temp

print("After Swap:\n")
print("a = " + str(a) + " and b = " + str(b))
