import math

def formula_general(a,b,c):
    descriminante = b**2 - 4*a*c
    if descriminante < 0:
        print("Es invalido, con raices imaginarias")
    else:
        x1 = (-b + math.sqrt(descriminante)) / (2 * a)
        x2 = (-b - math.sqrt(descriminante)) / (2 * a)
        print("X1 es", x1)
        print("X2 es", x2)


formula_general(1,4,4)
print("---------------")
formula_general(1,2,3)
print("---------------")
formula_general(1,0,-9)
print("---------------")
a = eval(input("Escribe el valor de a: "))
b = eval(input("Escribe el valor de a: "))
c = eval(input("Escribe el valor de a: "))
formula_general(a,b,c)