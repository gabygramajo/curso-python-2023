# Lista de números
numbers = [1, 2, 3, 4]

print(numbers)
# >> [1, 2, 3, 4]
print(type(numbers))
# >> <class 'list'>

# Lista de str
tasks = ['make a dishes', 'play videogames']

# indexing
print(f"Number List: {numbers[0]}")
print(f"Number List: {numbers[2]}")

print(f"tasks List: {tasks[0]}")
print(f"tasks List: {tasks[1]}")

# Las listas si son mutables:
tasks[0] = 'watch platzi courses'
print(tasks)
# >> ['watch platzi courses', 'play videogames']

# Slicing
print(tasks[1][5:])
# >> videogames