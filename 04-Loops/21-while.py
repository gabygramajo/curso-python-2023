# counter = 0

# while counter < 10:
#   counter += 1
#   print(counter)

# break para romper el flujo
# counter = 0
# while counter < 20:
#     counter += 1
#     if counter == 15:
#       break
#     print(counter)

# continue para saltar flujos
counter = 0
while counter < 10:
  counter += 1
  if counter%2 != 0:
    continue
  print(counter)