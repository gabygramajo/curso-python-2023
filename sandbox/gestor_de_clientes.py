clientes = {
    "12345678A": {
        "nombre": "Gustavo",
        "direccion": "Calle 1",
        "telefono": "111111111",
        "correo": "cliente1@example.com",
        "preferente": True
    },
    "23456789B": {
        "nombre": "Mariela",
        "direccion": "Calle 2",
        "telefono": "222222222",
        "correo": "cliente2@example.com",
        "preferente": True
    },
    "34567890C": {
        "nombre": "Juliana",
        "direccion": "Calle 3",
        "telefono": "333333333",
        "correo": "cliente3@example.com",
        "preferente": False
    },
    "45678901D": {
        "nombre": "Lucas",
        "direccion": "Calle 4",
        "telefono": "444444444",
        "correo": "cliente4@example.com",
        "preferente": True
    },
    "56789012E": {
        "nombre": "Miguel",
        "direccion": "Calle 5",
        "telefono": "555555555",
        "correo": "cliente5@example.com",
        "preferente": False
    }
}

# --- menu ---
def show_menu():
  print("¿Qué deseas Hacer?\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar.")
  while True:
    try:
      op = int(input("Elegir opción (1-6): "))
      if op >= 1 and op <= 6:
        return op
    except:
      print("Error! elije una Opción válida.\n")
    else:
      print("Elije una Opción válida.\n")

# --- op 1 ---
def add_client():
  nif = input("Ingresar NIF: ")
  new_client = { nif: {"nombre": None,
        "direccion": None,
        "telefono": None,
        "correo": None,
        "preferente": False}
        }
  new_client[nif]["nombre"] = input("Ingresar nombre: ")
  new_client[nif]["direccion"] = input("Ingresar direccion: ")
  new_client[nif]["telefono"] = input("Ingresar telefono: ")
  new_client[nif]["correo"] = input("Ingresar correo: ")
  new_client[nif]["preferente"] = input("Es preferente (true o false): ").capitalize()

  clientes.update(new_client)
  print(f"Cliente agregado exitosamente.")

# --- op 2 ---
def del_client():
  while True: 
    nif = input('Ingresar Nif del Cliente a eliminar (0=exit): ').upper()

    if nif == '0' or nif == "EXIT": 
      print("Saliendo del programa...")
      break
    if nif in clientes:
      print(f"Borrando el cliente: {clientes[nif]}")
      del clientes[nif]
      break
    print("cliente no encontrado, intente nuevamente.")

# --- op 3 ---
def show_client():
  while True: 
    nif = input('Ingresar Nif del Cliente a mostrar (0=exit): ').upper()

    if nif == '0' or nif == "EXIT": 
      print("Saliendo del programa...")
      break
    if nif in clientes:
      for date, value in clientes[nif].items():
        print(f"{date}: {value}")
      break
    print("cliente no encontrado, intente nuevamente.")

# --- op 4 ---
def show_all_client():
  for nif,dates in clientes.items():
    print(f"\n- NIF: {nif}")
    for date, value in dates.items():
        print(f"- {date.capitalize()}: {value}")

# --- op 5 ---
def show_preferents():
  clients = list(clientes.values())
  
  def its_preferens(client):
    if client["preferente"]:
      return True

  only_preferents = filter(its_preferens, clients)

  for x in only_preferents:
    print(x)

# ------- Main -------
def main():
  print(f"## GESTOR DE BBDD DE LOS CLIENTES {len(clientes)} DE LA EMPRESA ##")

  while True:
    op = show_menu()

    if op == 6:
      print("Saliendo del programa...")
      break
    elif op == 1:
      print("Ingrese los datos del cliente")
      add_client()
    elif op == 2:
      del_client()
    elif op == 3:
      show_client()
    elif op == 4:
      print("Mostrando todo los clientes...")
      show_all_client()
    elif op == 5:
      print("Mostrando clientes preferentes...")
      show_preferents()

# run
main()


