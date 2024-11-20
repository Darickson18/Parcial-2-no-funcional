class Dispositivo:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
    
class Iphone(Dispositivo):
    def __init__(self, modelo, precio, almacenamiento):
        super().__init__(modelo, precio)
        self.almacenamiento = almacenamiento

class Apple_Watch(Dispositivo):
    def __init__(self, modelo, precio, Wifi_o__celular):
        super().__init__(modelo, precio)
        self.wifi_o_celular = Wifi_o__celular