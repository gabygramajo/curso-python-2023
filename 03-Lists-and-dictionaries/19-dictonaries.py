my_dict = {}

print(f'my_dict: {type(my_dict)}')
# >> my_dict: <class 'dict'>

my_airplane_ticket = {
    'avion' : 'Aerolineas Argentinas',
    'name' : 'Nicolas',
    'last_name' : 'Molina Monroy',
    'age' : 73,
    'asiento': 'BN21'
}
print(f'my airplane ticket: {my_airplane_ticket}')
# >> my airplane ticket: {'avion': 'Aerolineas Argentinas', 'name': 'Nicolas', 'last_name': 'Molina Monroy', 'age': 73, 'asiento': 'BN21'}
print(f'len: {len(my_airplane_ticket)}')
# >> len: 5

#Accediendo a los valores mediante [llave] = valor:
print(f'name: {my_airplane_ticket["name"]}')
# >> name: Nicolas
print(f'lastname: {my_airplane_ticket["last_name"]}')
# >> lastname: Molina Monroy

# Comprobar si existe un valor
# print(f'Precio del pasaje: {my_airplane_ticket["precio"]}') # >> KeyError: 'precio'
print(f'Existe el precio del pasaje: {my_airplane_ticket.get("precio")}')
# >> Existe el precio del pasaje: None
print(f'Existe la edad: {"age" in my_airplane_ticket}')
# >> Existe la edad: True