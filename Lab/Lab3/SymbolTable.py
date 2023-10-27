from HashTable import HashTable

class SymbolTable:
    def __init__(self) -> None:
        self.hashTable = HashTable(size=10)

    def insert(self, element):
        try:
            i, pos = self.hashTable.search(element)
        except KeyError:
            i, pos = self.hashTable.insert(element)
        return (i, pos)

if __name__ == "__main__":
    SymTable = SymbolTable()
    elements = ["a", "b", "c", "d", "a", "aafas", "f"]
    for e in elements:
        print(e, " -> ", SymTable.insert(e))
