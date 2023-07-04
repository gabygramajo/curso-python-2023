
# for element in range(0,10):
#     print(element)


lista_mascotas = ['Perro', 'Gato', 'Conejo', 'Hamster', 'Loro', 'Caballo', 'Mono','Cuervo', 'Iguana', 'Cerdo']

# for element in lista_mascotas:
#     print(element)

producto = {
    'name': 'Camisa',
    'type': 'Indumentary',
    'price': '24.99',
    'stock': 100
}

# for key, value in producto.items():
#     print(f'{key} - {value}')

people = [
    {
        'name': 'nico',
        'age': 23
    },
    {
        'name': 'luisana',
        'age': 20
    },
    {
        'name': 'miguel',
        'age': 31
    },
    {
        'name': 'maria',
        'age': 24
    },
]

for person in people:
    for key, value in person.items():
        print(f'{key} - {value}')