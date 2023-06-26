name = "Nicolás"
last_name = "Molina Monroy"
print("name:", name)
print("last name:", last_name)

# Concatenando strings
full_name = name + " " + last_name
print("fullname:", full_name)

# Utilización de '' y "" en str
quote = "I'm Nicolás"
print(quote)

quote2 = ' She said "Hello" '
print(quote2)

# format
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)