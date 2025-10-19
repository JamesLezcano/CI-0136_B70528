from src.models.potion import Potion

class Elixir(Potion):
    def healing(self, target):
        HP = 10       
        target.heal(HP)   
        return f"{target.name} Toma una posion que aumenta {HP} de vida"