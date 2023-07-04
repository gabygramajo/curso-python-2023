lista_mascotas = ['Perro', 'Gato', 'Conejo', 'Hamster', 'Loro', 'Caballo']
print(f'1 - {lista_mascotas}')

# borrar conejo
lista_mascotas.pop(2)
print(f'2 - {lista_mascotas}')

# insert un elemento
lista_mascotas.insert(2, 'Mono')
print(f'3 - {lista_mascotas}')

# extender la lista
otros_animales = ['Cuervo', 'Iguana', 'Cerdo']
lista_mascotas.extend(otros_animales)
print(f'4 - {lista_mascotas}')

lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# completa el ejercicio
lista1.append(1234)
lista1.append('Hola')

lista2.append('Adiós')
lista2.append(1234)
print(lista1)
print(lista2)
lista3 = []
lista3.extend(lista1[0:len(lista1) - 1])
print(lista3)

lista4 = []
lista4.extend(lista2[1:len(lista2) - 1])
print(lista4)

lista5 = lista4 + lista3