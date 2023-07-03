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