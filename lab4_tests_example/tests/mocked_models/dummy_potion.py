from src.models.potion import Potion

class DummyPotion(Potion):
    def healing(self, target):
        """Crea una posion testing para el laboratorio"""      
        return f"{target.name} Toma una posion que de prueba que me permite sacar 100 en el laboratorio 4, jaja"