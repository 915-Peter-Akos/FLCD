class Pif:

    def __init__(self) -> None:
        self.__table = list()

    def add(self, token, pos):
        self.__table.append((token, pos))

    def size(self):
        return len(self.__table)
    
    def get_item(self, index):
        return self.__table[index]

    def get_all(self):
        return self.__table