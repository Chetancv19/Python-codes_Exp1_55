#Chetan Velonde 3019155
#Python Program to Convert Kilometers to Miles, Celsius To Fahrenheit and other conversions

a = int(input("Please Enter the operation to follow:\n 1. KM to miles\n 2. Celsius to Fahrenheit\n 3. Miles to KM\n 4. Fahrenheit to Celsius\n"))

if a == 1:
    l = float(input("Please enter the value to be converted from KM to miles (in kilometers): "))
    m = 0.621371*l
    print(str(l) + " kilometers is equal to "+str(m)+" Miles")
elif a == 2:
    c = float(input("Please enter the value to be converted from Celsius to Fahrenheit (in Celsius): "))
    f = (c*(9/5)) + 32
    print(str(c) + " Celsius is equal to " + str(f) + " Fahrenheit")
elif a == 3:
    m1 = float(input("Please enter the value to be converted from miles to KM (in miles): "))
    l1 = m1/0.621371
    print(str(m1) + " miles is equal to "+str(l1)+" Kilometers")
elif a == 4:
    f1 = float(input("Please enter the value to be converted from Fahrenheit to Celsius (in Fahrenheit): "))
    c1 = (f1-32)*(5/9)
    print(str(c1) + " Fahrenheit is equal to " + str(f1) + " Celsius")