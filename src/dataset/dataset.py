from abc import ABC, abstractmethod

class Dataset(ABC):
    @abstractmethod
    def preprocess(self):
        pass