from decimal import Decimal

a = 3.3 
print(f"a = {a}")
#>> a = 3.3

b = Decimal('1.1') + Decimal('2.2')
print(f"b = {b}")
#>> b = 3.3

print(f"a == b => {a == float(b)}")
#>> a == b => True
print(f"type a = {type(a)}")
#>> type a = <class 'float'>
print(f"type b = {type(b)}")
#>> type b = <class 'decimal.Decimal'>
