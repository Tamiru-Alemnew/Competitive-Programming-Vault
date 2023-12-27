import random

class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.elements = []

    def insert(self, value: int) -> bool:
        if value in self.index_map:
            return False
        self.index_map[value] = len(self.elements)
        self.elements.append(value)
        return True

    def remove(self, value: int) -> bool:
        if value not in self.index_map:
            return False
        index_to_remove, last_element = self.index_map[value], self.elements[-1]
        self.index_map[last_element], self.elements[index_to_remove] = index_to_remove, last_element
        self.elements.pop()
        self.index_map.pop(value)
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)
