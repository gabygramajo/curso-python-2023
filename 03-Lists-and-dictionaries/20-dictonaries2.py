person = {
  'name': 'nico',
  'last_name': 'Molina',
  'langs': ['python', 'javascript'],
  'age': 34
}
print(f'person: {person}')

# cambiando los valores:
person['name'] = 'santi'
person['age'] += 2
person['langs'].append('sql')
print(f'update person: {person}')

# Eliminar campo
carrera = {
  'toyota': 'Nicolas',
  'honda': 'Marcelo',
  'ford': 'Gustavo',
  'chevrolet': 'Luis',
  'fiat': 'maria'
}
print(carrera)
#op 1
del carrera['toyota']
#op2
carrera.pop('ford')

print(carrera)

# items, keys y values
print(f'Items: {person.items()}')
print(f'Keys: {person.keys()}')
print(f'Values: {person.values()}')

carrera['peugeot'] = 'luciano'
print(carrera)