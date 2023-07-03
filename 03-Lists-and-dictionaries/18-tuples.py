# TUPLAS ()

tupleNumbers = (1, 2, 3, 5)
tupleNames = ('nico', 'zule', 'santi')

print(f'tupleNumbers: {tupleNumbers}')
print(f'Pos 0: {tupleNumbers[0]}')
print(f'Pos -1: {tupleNumbers[-1]}')
print(f'Type: {type(tupleNumbers)}')

print(f'tupleNames: {tupleNames}')
print(f'Type: {type(tupleNames)}')

'''Las tuplas son estructuras de datos inmutables, una vez declaras e iniciadas ya no pueden ser modificadas'''

# Las tuplas cuentan con dos métodos:
print(f'tupleNumbers Count "3": {tupleNumbers.count(3)}')
print(f'tupleNames Count "zule": {tupleNames.count("zule")}')

print(f'Index of "zule": {tupleNames.index("zule")}')

# Tuple to List
listNames = list(tupleNames)
print(f'listNames: {listNames}')
print(f'Type: {type(listNames)}')

listNames.append('alfredo')
newTupleNames = tuple(listNames)
print(f'newTupleNames: {newTupleNames}')