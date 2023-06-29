text = 'voy a ser un Data Engineer'
print(f'text = {text}')


'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''

print(f'Todo a Mayúscula: {text.upper()}')
print(f'Todo a Minúscula: {text.lower()}')
print(f'Capitalize: {text.capitalize()}')
print(f'Tamaño: {len(text)}')
print(f'Cuántas veces tiene la "a": {text.count("a")}')

print(f'Swap mayúsculas y minúsculas: {text.swapcase()}')
print(f'Comienza con "voy"?: {text.startswith("voy")}')
print(f'Termina con "Data"?: {text.endswith("Data")}')
print(f'Reemplazar Engineer por Analyst: {text.replace("Engineer", "Analyst")}')
print(f'Tipo Título: {text.title()}')

# Los str son inmutables
text[5] = 'perro'
# >> TypeError: 'str' object does not support item assignment