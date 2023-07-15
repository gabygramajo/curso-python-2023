set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Unión de Conjuntos - op 1
set_c = set_a.union(set_b)
print( set_c )
# >> {'bol', 'mex', 'pe', 'col'}

# Unión de Conjuntos - op 2
set_c = set_a | set_b
print( set_c )
# >> {'bol', 'mex', 'pe', 'col'}

# Intersección de Conjuntos op 1
elements_in_common = set_a.intersection(set_b)
print(elements_in_common)
# >> {'bol'}

# Intersección de Conjuntos op 2
elements_in_common = set_a & set_b 
print(elements_in_common)
# >> {'bol'}

# Diferencia de Conjuntos op 1
diference_a_b = set_a.difference(set_b)
print(diference_a_b)
# >> {'col', 'mex'}

# Diferencia de Conjuntos op 2
diference_a_b = set_a - set_b
print(diference_a_b)
# >> {'col', 'mex'}

# Diferencia Simétrica de Conjuntos op 1
symmetric_diference_a_b = set_a.symmetric_difference(set_b)
print(symmetric_diference_a_b)
# >> {'col', 'pe', 'mex'}

# Diferencia Simétrica de Conjuntos op 2
symmetric_diference_a_b = set_a ^ set_b
print(symmetric_diference_a_b)
# >> {'col', 'pe', 'mex'}