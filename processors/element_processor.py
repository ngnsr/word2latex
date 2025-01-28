from abc import ABC, abstractmethod

class ElementProcessor(ABC):
    @abstractmethod
    def process(self, element) -> str:
        pass
