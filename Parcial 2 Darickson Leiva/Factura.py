class Factura:
    def __init__(self, nombre_y_apellido, cedula, dispositivos, monto):
        self.nombre_y_apellido = nombre_y_apellido
        self.cedula = cedula
        self.dispositivos = dispositivos
        self.monto = monto

    def mostar_reporte_clientes(self):
        print()
        print(f"Nombre: {self.nombre_y_apellido}")
        print(f"Cedula: {self.cedula}")
        print(f"Dispositivos Comprados: {self.dispositivos}")
        print(f"Monto: {self.monto}")
        print()