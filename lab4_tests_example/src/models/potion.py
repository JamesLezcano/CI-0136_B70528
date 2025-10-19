from abc import ABC, abstractmethod

class Potion(ABC):
    @abstractmethod
    def healing(self, target):
        pass