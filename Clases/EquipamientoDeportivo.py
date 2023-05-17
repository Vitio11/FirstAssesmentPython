from abc import ABC, abstractmethod

class EquipamientoDeportivo(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    @abstractmethod
    def descripcion(self):
        pass

class EquipamientoFutbol(EquipamientoDeportivo):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla
    
    def descripcion(self):
        return f"{self.nombre} talla {self.talla} para futbol, precio: {self.precio}"

class EquipamientoBasketball(EquipamientoDeportivo):
    def __init__(self, nombre, precio, talla, material):
        super().__init__(nombre, precio)
        self.talla = talla
        self.material = material
    
    def descripcion(self):
        return f"{self.nombre} talla {self.talla} para basketball, hecho de {self.material}, precio: {self.precio}"

class EquipamientoRugby(EquipamientoDeportivo):
    def __init__(self, nombre, precio, peso):
        super().__init__(nombre, precio)
        self.peso = peso
    
    def descripcion(self):
        return f"{self.nombre} con peso de {self.peso} para rugby, precio: {self.precio}"

