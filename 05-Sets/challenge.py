countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}
new_set = set()
# Escribe tu solución 👇
new_set.update(countries, northAm, centralAm, southAm)

print(new_set)
# >> {'BZ', 'USA', 'ARG', 'GT', 'COL', 'CANADA', 'MX'}

new_set.intersection(countries, northAm, centralAm, southAm)

print(new_set)
# >>