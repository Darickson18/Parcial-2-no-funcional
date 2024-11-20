from Usuario import Usuario
from Dispositivo import Iphone, Apple_Watch
from Factura import Factura

class Apple:
    def __init__(self):
        self.producto = []
        self.usuarios = []
        self.compras = []

    def start(self):
        while True:
            print("Bienvenido al sistema de ventas de Apple Inc.")
            print("Por favor seleccione una de las siguientes opciones: \n1. Registrar dispositivos en el catálogo \n2. Registrar usuarios \n3. Registrar compras \n4. Reporte Clientes")
            menu = input("---> ")

            if menu == '1':
                self.registrar_dispositivo()
            elif menu == '2':
                self.registrar_usuario()
            elif menu == '3':
                self.registrar_compra()
            elif menu == '4':
                self.mostar_reporte_clientes()
            else:
                print("Ha ingresado una opción invalida, por favor intentelo de nuevo")

    def registrar_dispositivo(self):
        self.producto = []
        nuevo_dispositivo = input("Por favor ingrese el tipo del nuevo dispositivo: ")
        if nuevo_dispositivo == 'Iphone':
            modelo = input("Por favor ingrese el modelo del Iphone: ")
            precio = int(input("Por favor indique el precio que tendrá este modelo. Nota: el precio debe ser mayor a 700$: "))
            if precio < 700:
                print("Ha ingresado un precio invalido, por favor intentelo de nuevo.")
            else:
                print("Por favor elija la capacidad de almacenamiento que tendrá este dispositivo: \n1. 64 GB \n2. 128 GB \n3. 256 GB")
                opcion = input("---> ")
                if opcion == '1':
                    almacenamiento = '64 GB'
                elif opcion == '2':
                    almacenamiento = '128 GB'
                elif opcion == '3':
                    almacenamiento = '256 GB'
                print("Dispositivo registrado exitosamente!")

            Dispositivo_Apple = Iphone(modelo, precio, almacenamiento)
            self.producto.append(Dispositivo_Apple)

        elif nuevo_dispositivo == 'Apple Watch':
            modelo = input("Por favor ingrese el modelo del Apple Watch: ")
            precio = int(input("Por favor indique el precio que tendrá este modelo. Nota: el precio debe ser mayor a 300$: "))
            if precio < 300:
                print("Ha ingresado un precio invalido, por favor intentelo de nuevo.")
            else:
                print("Por favor elija si el Apple Watch funciona se conecta al wi-fi: \n1. Por si solo \n2. A través de su teléfono")
                opcion = input("---> ")
                if opcion == '1':
                    wifi_o_celular = 'wi-fi'
                elif opcion == '2':
                    wifi_o_celular = 'Celular'
                print("Dispositivo registrado exitosamente!")
        else:
            print("Ha ingresado una opción invalida, por favor intentelo de nuevo")

            Dispositivo_Apple = Apple_Watch(modelo, precio, wifi_o_celular)
            self.producto.append(Dispositivo_Apple)    

    def registrar_usuario(self):
        self.usuarios = []
        nombre_y_apellido = input("Por avor ingrese su nombre y apellido: ")
        cedula = input("Por favor ingrese su cedula de identidad: ")
        
        print("Usuario registrado exitosamente!")
        cliente = Usuario(nombre_y_apellido, cedula)
        self.usuarios.append(cliente)

    def registrar_compra(self):
        self.compras = []
        dispositivos = []
        monto = 0
        nombre_y_apellido = input("Por avor ingrese su nombre y apellido: ")
        cedula = input("Por favor ingrese su cedula de identidad: ")
        cantidad_dispositivos = input("Por favor ingrese cuantos dispositivos desea comprar. Si desea comprar mas de uno ingrese (+2)): ")
        if cantidad_dispositivos == '1':
            dispositivo = input("Por favor ingrese el dispositivo que desea comprar: ")
            if dispositivo == "Iphone":
                dispositivos.append(dispositivo)
                monto += 999
                
            elif dispositivo == "Apple Watch":
                dispositivos.append(dispositivo)
                monto += 399
        elif cantidad_dispositivos == "+2":
            ans = 'y'
            while ans == 'y':
                dispositivo = input("Por favor ingrese el dispositivo que desea comprar: ")
                if dispositivo == "Iphone":
                    dispositivos.append(dispositivo)
                    monto += 999
                    ans = input("Desea continuar? (y/n): ")
                elif dispositivo == "Apple Watch":
                    dispositivos.append(dispositivo)
                    monto += 399
                    ans = input("Desea continuar? (y/n): ")

        else:
            print("Ha ingresado una opción invalida, por favor intentelo de nuevo.")
        print("Compra registrado exitosamente!")
        compra = Factura(nombre_y_apellido, cedula, dispositivos, monto)
        self.compras.append(compra)

    def mostar_reporte_clientes(self):
        print()
        print(f"Nombre: {self.compras.nombre_y_apellido}")
        print(f"Cedula: {self.compras.cedula}")
        print(f"Dispositivos Comprados: {self.compras.dispositivos}")
        print(f"Monto: {self.compras.monto}")
        print()