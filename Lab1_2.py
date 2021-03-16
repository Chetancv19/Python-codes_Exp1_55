#Chetan Velonde 3019155
#Python Program to Solve Quadratic Equations
import math
print("PLease enter the coefficients of the quadratic equations: ")
a = int(input("Coefficient of X^2: "))
b = int(input("Coefficient of X: "))
c = int(input("Coefficient of X^0 or value of constant: "))

print("The quadratic equation is " + str(a) + "X^2 + " + str(b) + "X + " + str(c) + " = 0")

d = (b**2) - (4*a*c)
print(d)
if d >= 0:
    r1 = ((-b) + math.sqrt(d))/ (2 * a)
    r2 = ((-b) - math.sqrt(d)) / (2 * a)
    print("The value of the roots obtained is " + str(r1) + " and " + str(r2) + " respectively")

else:
    print("Roots are complex")
    e = math.sqrt(abs(d))
    f = (-b)/2
    print("The value of the roots obtained is " + str(round(f,2)) + "+i" + str(round(e,2)) + " and " + str(round(f,2)) + "-i" + str(round(e,2)) + " respectively")