# Dictionary Comprehension
# Generar una Dictionary a partir de un iterable

# Ej 1
dict = {n: n*2 for n in range(1, 5)}
print(dict)
# >> {1: 2, 2: 4, 3: 6, 4: 8}

# Ej 2
countries = ['col', 'mex', 'bol', 'pe']
population = ['50.4 millones de habitantes', '126.2 millones de habitantes', '11.8 millones de habitantes', '33.1 millones de habitantes']

countries_population = {countrie: population[i] for i,countrie in enumerate(countries)}
print(countries_population)
"""
{'col': '50.4 millones de habitantes', 
'mex': '126.2 millones de habitantes', 
'bol': '11.8 millones de habitantes', 
'pe': '33.1 millones de habitantes'}
"""

# Ej 2
# Unir listas con el método Zip
names = ['nico', 'zule', 'zoe']
ages = [32, 25, 28]
print( list( zip(names, ages) ) )
# >> [('nico', 32), ('zule', 25), ('zoe', 28)]

names_ages = { name: age for (name, age) in zip(names, ages) }
print(names_ages)
# >> {'nico': 32, 'zule': 25, 'zoe': 28}

# Dictionary Comprehension with conditionals
names = ['alice','nico', 'zule', 'zoe', 'lucia', 'luis','sol', 'lucas']
ages = [32,12,25, 11, 28, 9, 15, 16, 21]

# Ej 1
adults = { name: age for (name, age) in zip(names, ages) if age >= 18}
print(adults)
# >> {'alice': 32, 'zule': 25, 'lucia': 28}

minors = { name: age for (name, age) in zip(names, ages) if age < 18}
print(minors)
# >> {'nico': 12, 'zoe': 11, 'luis': 9, 'sol': 15, 'lucas': 16}

text = 'Python es un lenguaje de tipado estatico'
unique = { c.lower(): c.upper() for c in text if c.lower() in 'aeiou' }
print(unique)
# >> {'o': 'O', 'e': 'E', 'u': 'U', 'a': 'A', 'i': 'I'}

unique_count = { c: text.count(c) for c in text if c.lower() in 'aeiou' }
print(unique_count)
# >> {'o': 3, 'e': 5, 'u': 2, 'a': 3, 'i': 2}