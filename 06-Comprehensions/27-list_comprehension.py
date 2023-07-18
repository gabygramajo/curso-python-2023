# List Comprehension
# Generar una lista a partir de un iterable

# Forma clásica
numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creando una List Comprehension
lc_numbers = [element for element in range(1, 11)]
print(lc_numbers)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Su utilidad principal es la facil lectura y ahorro de codigo

# otro ejemplo
lc_numbers = [element*2 for element in range(1, 11)]
print(lc_numbers)
# >> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# utilizando condicional en List Comprehesion
pair_numbers = [n*2 for n in range(1, 11) if n % 2 == 0]
print(pair_numbers)
# >> [4, 8, 12, 16, 20]