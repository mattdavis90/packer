class Bin(object):
    def __init__(self):
        self.weight = 0
        self.value = 0
        self.items = []

    def add_item(self, item):
        self.weight += item.weight
        self.value += item.value
        self.items.append(item)
