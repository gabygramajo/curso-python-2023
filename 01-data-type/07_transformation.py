name = "Nicolas"
print(type(name))
# cambiando el tipo de forma dinámica
name = 12
print(type(name))
# Number a boolean
name = True
print(type(name))
# esto se considera una malapráctica y no se debe hacer
print('12' + '15')
# print('12' + 1) error

# ej 1

age = 43
"""
print("Mi edad es " + age)
Traceback (most recent call last):
  File "/home/runner/Python101/07_transformation.py", line 13, in <module>
    print("Mi edad es " + age)
TypeError: can only concatenate str (not "int") to str
"""
# forma correcta
print("Mi edad es " + str(age))
# o
print(f"Mi edad es {age}")

# EJ 2
age = input("Ingresa tu edad: ")
print(type(age))

age = int(age)
print(f"Tu edad en 10 años sera {age + 10}")