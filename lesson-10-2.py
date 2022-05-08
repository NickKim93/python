class Clothes:
    def __init__(self, price, brand=""):
        self._brand = brand
        self._price = price

    @property
    def price(self):
        return self._price


class Coat(Clothes):
    def __init__(self, price, brand, size):
        super().__init__(price, brand)
        self.size = size

    def consume(self):
        fabric = float(self.size) / 6.5 + 0.5
        print(f'Fabric required for tailoring {self._brand} {self.__class__.__name__}: {fabric:.2f}')
        return fabric


class Suit(Clothes):
    def __init__(self, price, brand, height):
        super().__init__(price, brand)
        self.height = height

    def consume(self):
        fabric = float(self.height) / 6.5 + 0.5
        print(f'Fabric required for tailoring {self._brand} {self.__class__.__name__}: {fabric:.2f}')
        return fabric


item_1 = Coat(23000, 'Zara', '46')
item_2 = Suit(19000, 'H&M', '170')
item_1.consume()
item_2.consume()
print(item_1.price)
item_1.price = 230000
