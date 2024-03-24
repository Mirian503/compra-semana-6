from ownable import Ownable  # Importar el módulo Ownable

class Cart(Ownable):
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)