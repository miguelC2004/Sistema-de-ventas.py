# Crear un diccionario con la información de los vuelos
vuelos = {
  "VUELO_1": {
    "ruta": "Nueva York - Los Ángeles",
    "horario": "12:00",
    "precio": 200
  },
  "VUELO_2": {
    "ruta": "Chicago - Miami",
    "horario": "14:00",
    "precio": 250
  },
  "VUELO_3": {
    "ruta": "San Francisco - Nueva York",
    "horario": "16:00",
    "precio": 300
  }
}

# Crear una función para mostrar la información de un vuelo
def mostrar_vuelo(codigo):
  vuelo = vuelos[codigo]
  print(f"Ruta: {vuelo['ruta']}")
  print(f"Horario: {vuelo['horario']}")
  print(f"Precio: ${vuelo['precio']}")

# Crear una función para comprar un ticket
def comprar_ticket(codigo):
  vuelo = vuelos[codigo]
  precio = vuelo['precio']
  confirmacion = input(f"¿Deseas comprar un ticket para el vuelo {vuelo['ruta']} por ${precio}? (S/N) ")
  if confirmacion.upper() == "S":
    print("Gracias por tu compra!")
  else:
    print("Operación cancelada.")

# Mostrar el menú de opciones al usuario
opcion = 0
while opcion != 4:
  print("1. Ver vuelos disponibles")
  print("2. Mostrar información de un vuelo")
  print("3. Comprar ticket")
  print("4. Salir")
  opcion = int(input("Selecciona una opción: "))

  # Mostrar el menú de opciones al usuario
opcion = 0
while opcion != 4:
  print("1. Ver vuelos disponibles")
  print("2. Mostrar información de un vuelo")
  print("3. Comprar ticket")
  print("4. Salir")
  opcion = int(input("Selecciona una opción: "))

  if opcion == 1:
    # Mostrar todos los vuelos
    for codigo, vuelo in vuelos.items():
      print(codigo)
      print(f"Ruta: {vuelo['ruta']}")
      print(f"Horario: {vuelo['horario']}")
      print(f"Precio: ${vuelo['precio']}\n")

  elif opcion == 2:
    # Mostrar la información de un vuelo específico
    codigo = input("Ingresa el código del vuelo que deseas ver: ")
    mostrar_vuelo(codigo)

  elif opcion == 3:
    # Comprar un ticket
    codigo = input("Ingresa el código del vuelo para el que deseas comprar un ticket: ")
    comprar_ticket(codigo)

  elif opcion == 4:
    # Salir del programa
    print("Gracias por utilizar nuestro sistema de ventas. ¡Hasta pronto!")
