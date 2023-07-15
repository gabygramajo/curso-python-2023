# números enteros
lives = 3
age = 43
budget = 2000

# números flotante
temperature = 12.23
price = 99.99
# print(type(temperature))
# print(type(price))

# OPERACIONES

armor = 15
damage = 2
print(f"initial armor = {armor}")


armor = armor - damage
print(f"-damageX1, current armor = {armor}")

armor -= damage
armor -= damage
print(f"-damageX2, current armor = {armor}")

regeneration = 1
armor += regeneration
armor += regeneration
print(f"+regenerationX2, current armor = {armor}")

# Notación científica
big_number = 45000000000000000000.1
print(big_number)

small_number = 0.00000000000000000000023
print(small_number)

# Challenge
january_budget = 1200
february_budget = 2000
march_budget = 1500

average = (january_budget + february_budget + march_budget) / 3

print("average of my quarterly budget = $", round(average))