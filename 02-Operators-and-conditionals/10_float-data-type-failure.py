x = 3.3 
print(x)
# >> 3.3
y = 1.1 + 2.2
print(y)
# >> 3.3000000000000003

print(x == y)
# >> False

# OP1
# formateamos a dos digitos. Pero lo convierte a tipo str
y_str = format(y, ".2g")
print('str =>', y_str)
# >> str => 3.3
print(y_str == str(x))
# >> True

# OP2
# Creamos margen te dolerancia.
tolerance = 0.00001
print(abs(x - y) < tolerance)
# >> True

# OP3
# utilizando el método round para redondear un numero
print(x == round(y, 1))
# >> True

"""
La falla que mencionas no es específica de Python, sino que está relacionada con el punto flotante y cómo se representan los números en la computadora. Este problema se debe a que los números de punto flotante se almacenan en una cantidad finita de bits y, en algunos casos, puede haber una pérdida de precisión.

En el caso de la expresión "1.1 + 2.2", el resultado debería ser 3.3. Sin embargo, debido a la forma en que se representan los números de punto flotante en la computadora, el resultado en Python (y en muchos otros lenguajes de programación) es un valor ligeramente diferente: 3.3000000000000003.

Esto ocurre porque los números de punto flotante se representan en la computadora utilizando una técnica llamada aritmética de coma flotante, que no puede representar todos los números racionales exactamente. Los números decimales como 1.1 y 2.2 tienen representaciones binarias infinitas, y la conversión entre la representación decimal y la binaria puede introducir pequeños errores.

Es importante tener en cuenta que esta pérdida de precisión es inherente a la forma en que se manejan los números de punto flotante en la mayoría de las computadoras, y no es exclusiva de Python. Para evitar este problema en situaciones donde se requiere alta precisión, es posible utilizar bibliotecas especializadas de números decimales o fraccionarios en Python.
n Python, existen dos bibliotecas principales para manejar números decimales y fraccionarios con alta precisión: decimal y fractions.
"""
