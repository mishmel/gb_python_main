from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v
    @property
    def tissue_consumption(self):
        r = (self.v/6.5) + 0.5
        r = round(r, 3)
        return r

class Costume(Clothes):

    def __init__(self, h):
        self.h = h
    @property
    def tissue_consumption(self):
        r = (2 * self.h + 0.3)
        r = round(r, 3)
        return r

costume = Costume(5.003)
coat = Coat(6)
print(coat.tissue_consumption)
print(costume.tissue_consumption)
