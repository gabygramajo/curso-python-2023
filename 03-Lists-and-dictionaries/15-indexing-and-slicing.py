text = 'Ella sabe Python'


# Indexing: los str están indexados del 0 al len() - 1, al cual podemos acceder a un determinado caracter por su indice.
# 1er caracter
print(text[0])
# >> E
print(text[10])
# >> P
"""
print(text[1000])
# >>
Traceback (most recent call last):
  File "15-indexing.py", line 5, in <module>
    print(text[1000])
IndexError: string index out of range
"""

# Accediendo al último caracter:
# op1
size = len(text)
print(f"Size: {size}")
# >> 16
print(text[size - 1])
# >> n

# op2
print(text[-1])
# >> n

# Slicing: mediante el slicing podemos rebanar los str y mostrar solo una parte.
# str[incluyente : no incluyente]
print(text[0:5])
# >> Ella
print(text[10:15])
# >> Pytho
print(text[0:8])
# >> Ella sab
print(text[:])
# >> Ella sabe Python

# str[incluyente : no incluyente : n°de saltos]
print(text[10:16])
# >> Python

# Un salto desde el inicio
print(text[10:16:1])
# >> Python

# Dos salto desde el inicio
print(text[10:16:2])
# >> Pto

# Del inicio al final con 2 saltos
print(text[::2])
# >> El aePto

# Invertir string
print(text[::-1])
# >> nohtyP ebas allE

# Invertir
print(text[16:9:-1])
# >> nohtyP

# indices negativos
print(text[-5:-2])
# >> yth