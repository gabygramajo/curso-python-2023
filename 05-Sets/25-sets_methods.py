set_countries = {'col', 'mex', 'bol', 'col'}

# Tamaño
size = len(set_countries)
print(size)
# >> 3

# Elemento especifico
print('col' in set_countries)
# >> True
print('pe' in set_countries)
# >> False

# Agregar elemento
set_countries.add('pe')
print(set_countries)
# >> {'col', 'bol', 'mex', 'pe'}

# Actualizar
set_countries.update({'arg', 'ecu', 'pe'})
print(set_countries)
# >> {'pe', 'mex', 'col', 'ecu', 'ar', 'bol'}

# Eliminar elemento
set_countries.remove('col')
set_countries.remove('arg')
print(set_countries)
# >> {'bol', 'ecu', 'mex', 'pe'}

# Eliminar elemento que no existe, arroja error.
"""set_countries.remove('bra')
# >>
Traceback (most recent call last):
  File "25-sets_methods.py", line 31, in <module>
    set_countries.remove('bra')
KeyError: 'bra'
"""

# Eliminar elemento y si no existe, no arroja error.
set_countries.discard('pay')
print(set_countries)
# >> {'bol', 'mex', 'pe', 'ecu'}

# Eliminar todo
set_countries.clear()
print(set_countries)
# >> set()
print(len(set_countries))
# >> 0

# Ordernar alfabéticamente
"""Un detalle a tener en cuenta es que al usar sorted() no nos retorna un conjunto, sino una Lista. Si volvemos a convertirlos a Set volveriamos a perder el orden, ya que los conjuntos no tienen un orden."""
set_countries = {'col', 'bol', 'mex'}
countries_sorted = sorted( set_countries )
print(countries_sorted)
# >> ['bol', 'col', 'mex']

set_countries_sorted = set( countries_sorted )
print(set_countries_sorted)
# >> {'mex', 'bol', 'col'}