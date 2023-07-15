"""
Los Sets - Conjutos 
- Se pueden modificar.
- No tienen un orden
- No permite duplicados
"""

set_countries = {'col', 'mex', 'bol', 'col'}
print(set_countries)
# >> {'mex', 'col', 'bol'}
print(type(set_countries))
# >> <class 'set'>

set_numbers = {1, 2, 443, 2, 23}
print(set_numbers)
# >> {1, 2, 443, 23}

set_types = {1, 'hola', False, 12.12}
print(set_types)
# >> {False, 1, 'hola', 12.12}

set_from_string = set('hola')
print(set_from_string)
# >> {'o', 'a', 'l', 'h'}

set_from_string = set('hoollaaaa')
print(set_from_string)
# >> {'o', 'a', 'l', 'h'}

set_from_tuples = set( ('abc', 'cbv', 'as', 'abc') )
print(set_from_tuples)
# >> {'cbv', 'abc', 'as'}

numbers = [1, 2, 3, 1, 2, 3, 4]
set_from_list = set( numbers )
print(set_from_list)
# >> {1, 2, 3, 4}

list_from_set = list(set_from_list)
print(list_from_set)
# >> [1, 2, 3, 4]