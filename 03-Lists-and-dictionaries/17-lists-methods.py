# CRUD Create, Read, Update & Delete.

numbers = [1, 2, 3, 4, 5]
print(numbers)
# >> [1, 2, 3, 4, 5]

print(numbers[1])
# >> 2
numbers[-1] = 10
print(numbers)
# >> [1, 2, 3, 4, 10]

# Agregar elementos al final de la lista:
numbers.append(700)
print(numbers)
# >> [1, 2, 3, 4, 10, 700]

# Insertar elementos en una posición determinada de la lista:
numbers.insert(1, 231)
print(numbers)
# >> [1, 231, 2, 3, 4, 10, 700]

# Fusionar listas
tasks = ['todo 1', 'todo 2', 'todo 3']

new_list = numbers + tasks
print(new_list)
# >> [1, 231, 2, 3, 4, 10, 700, 'todo 1', 'todo 2', 'todo 3']

# Buscar posicion de un elemento
print(f'todo 2 index: {new_list.index("todo 2")}')
# >> todo 2 index: 8

index = new_list.index("todo 2")
new_list[index] = 'todo 2 - done'
print(new_list)
# >> [1, 231, 2, 3, 4, 10, 700, 'todo 1', 'todo 2 - done', 'todo 3']

# Remover elemento
new_list.remove(new_list[index])
print(new_list)
# >> [1, 231, 2, 3, 4, 10, 700, 'todo 1', 'todo 3']

# Remover el último elemento
new_list.pop()
print(new_list)
# >> [1, 231, 2, 3, 4, 10, 700, 'todo 1']

new_list.pop()
print(new_list)
# >> [1, 231, 2, 3, 4, 10, 700]

# Voltear un array
new_list.reverse()
print(new_list)
# >> [700, 10, 4, 3, 2, 231, 1]

# Ordenar una lista
unordered_numbers = [2, 5,3, 1, 0]
new_list.sort()
print(unordered_numbers)
# >> [2, 5, 3, 1, 0]

unordered_str = ['u','e', 'o', 'a', 'i']
unordered_str.sort()
print(unordered_str)
# >> ['a', 'e', 'i', 'o', 'u']
