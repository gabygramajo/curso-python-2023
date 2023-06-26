# >
print(f" 4 > 2 = {4 > 2}")
print(f" 4 > 5 = {4 > 5}")
print(f" 5 > 5 = {5 > 5}\n")

# <
print(f" 4 < 2 = {4 < 2}")
print(f" 4 < 5 = {4 < 5}")
print(f" 5 < 5 = {5 < 5}\n")

# >= 
print(f" 4 >= 2 = {4 >= 2}")
print(f" 4 >= 5 = {4 >= 5}")
print(f" 5 >= 5 = {5 >= 5}\n")

# <=
print(f" 4 <= 2 = {4 <= 2}")
print(f" 4 <= 5 = {4 <= 5}")
print(f" 5 <= 5 = {5 <= 5}\n")

# ==
print(f" 4 == 2 = {4 == 2}")
print(f" 4 == 5 = {4 == 5}")
print(f" 5 == 5 = {5 == 5}\n")

# !=
print(f" 4 != 2 = {4 != 2}")
print(f" 4 != 5 = {4 != 5}")
print(f" 5 != 5 = {5 != 5}\n")

# comparando entre diferentes tipo de datos
print(f" '2' == 2 = {'2' == 2}") # false
print(f" '2' == 'A' = {'2' == 'A'}") # False
print(f" '2' > 'A' = {'2' > 'A'}") # False
print(f" '2' < 'A' = {'2' < 'A'}") # True
print(f" 'a' > 'A' = {'a' > 'A'}") # True
print(f" 'a' < 'A' = {'a' < 'A'}") # False

#print(f" '2' < 2 = {'2' < 2}") TypeError: '<' not supported between instances of 'str' and 'int'
#print(f" '2' >= 2 = {'2' >= 2}") TypeError: '>=' not supported between instances of 'str' and 'int'
#print(f" '2' <= 2 = {'2' <= 2}") TypeError: '>=' not supported between instances of 'str' and 'int'