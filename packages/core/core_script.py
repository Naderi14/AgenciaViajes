import os

listaDestinos = []
listaCustomers = []
listaBookings = []

def AddDestino():
    # Input codigo destino
    while True:
        codigoDestino = input("Introduzca el código identificativo del nuevo destino ---> : ").upper()
        if codigoDestino == None or codigoDestino == "":
            print("\n<---((( ¡¡El código no puede quedar vacío!! )))--->\n")
        elif codigoDestino.isnumeric():
            print("\n<---((( ¡¡El código no puede ser un número!! )))--->\n")
        else:
            break
    # Input nombre destino
    while True:
        nameDestino = input("Introduzca el nombre del nuevo destino ---> : ").title()
        if nameDestino == None or nameDestino == "":
            print("\n<---((( ¡¡El nombre no puede quedar vacío!! )))--->\n")
        elif nameDestino.isnumeric():
            print("\n<---((( ¡¡El nombre no puede ser un número!! )))--->\n")
        else:
            break
    # Input precio destino
    while True:
        precioDestino = input("Introduzca el precio del nuevo destino ---> : ")
        if precioDestino.isnumeric():
            precioDestino = float(precioDestino)
            break
        else:
            print("\n<---((( ¡¡El precio tiene que ser un número además de valor positivo!! )))--->\n")
    # Creamos diccionario
    nuevoDestino = {
        'codigo' : codigoDestino, #string
        'nombre' : nameDestino, #string
        'precio' : precioDestino #float
        }
    # Añadimos el diccionario a la lista
    listaDestinos.append(nuevoDestino)
    
def AddCustomer():
    # Asignamos ID al nuevo cliente
    id = len(listaCustomers) + 1
    # Input nombre cliente
    while True:
        nombreCliente = input("Introduzca el nombre del nuevo cliente ---> : ").title()
        if nombreCliente == None or nombreCliente == "":
            print("\n<---((( ¡¡El nombre del cliente no puede quedar vacío!! )))--->\n")
        elif nombreCliente.isnumeric():
            print("\n<---((( ¡¡El nombre del cliente no puede ser un número!! )))--->\n")
        else:
            break
    # Creamos diccionario
    nuevoCliente = {
        'ID' : id, #int
        'nombre' : nombreCliente #string
    }
    # Añadimos el diccionario a la lista
    listaCustomers.append(nuevoCliente)

def AddBooking():
    # Input codigo destino
    codigoOK = False
    idOK = False
    while codigoOK == False:
        codigoDestino = input("Introduzca el código identificativo del nuevo destino ---> : ").upper()
        if codigoDestino == None or codigoDestino == "":
            print("\n<---((( ¡¡El código no puede quedar vacío!! )))--->\n")
        elif codigoDestino.isnumeric():
            print("\n<---((( ¡¡El código no puede ser un número!! )))--->\n")
        else:
            for destino in listaDestinos:
                if codigoDestino == destino['codigo']:
                    codigoOK = True
                else:
                    print("\n<---((( ¡¡El código no coincide con ningún destino en la base de datos!! )))--->\n")
    # Input nombre cliente
    while idOK == False:
        idCliente = input("Introduzca el nombre del nuevo cliente ---> : ").title()
        if idCliente == None or idCliente == "":
            print("\n<---((( ¡¡El nombre del cliente no puede quedar vacío!! )))--->\n")
        elif idCliente.isnumeric():
            print("\n<---((( ¡¡El nombre del cliente no puede ser un número!! )))--->\n")
        else:
            for cliente in listaCustomers:
                if idCliente == cliente['ID']:
                    idOK = True
                else:
                    print("\n<---((( ¡¡El ID no coincide con ningún cliente en la base de datos!! )))--->\n")
    # Creamos diccionario
    nuevoBooking = {
        'codigo' : codigoDestino,
        'ID' : idCliente
    }
    # Añadimos el diccionario a la lista
    listaBookings.append(nuevoBooking)
   
def CancelBooking():
    # Input codigo destino
    while True:
        codigoDestino = input("Introduzca el código identificativo del nuevo destino ---> : ").upper()
        if codigoDestino == None or codigoDestino == "":
            print("\n<---((( ¡¡El código no puede quedar vacío!! )))--->\n")
        elif codigoDestino.isnumeric():
            print("\n<---((( ¡¡El código no puede ser un número!! )))--->\n")
        else:
            break
    # Input ID Cliente
    while True:
        idCliente = input("Introduzca el nombre del nuevo cliente ---> : ").title()
        if idCliente == None or idCliente == "":
            print("\n<---((( ¡¡El nombre del cliente no puede quedar vacío!! )))--->\n")
        elif idCliente.isnumeric():
            print("\n<---((( ¡¡El nombre del cliente no puede ser un número!! )))--->\n")
        else:
            break
    # Buscamos si existe la reserva, si existe la cancelamos
    for reserva in listaBookings:
        if codigoDestino == reserva['codigo'] and idCliente == reserva['ID']:
            print(f"La reserva ")
            listaBookings.remove(reserva)
    
    
        

for producto in inventario:
    if productoID == producto['ID']:
        us.limpiarConsola()
        print(f"Se ha borrado del inventario: {producto['NombreProducto']}\n")
        inventario.remove(producto)
    else:
        us.limpiarConsola()
        print(f"No se ha encontrado ningún producto con ID #{productoID}\n")