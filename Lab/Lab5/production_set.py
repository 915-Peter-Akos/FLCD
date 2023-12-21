class ProductionSet:

    def __init__(self):
        self.__productions = []

    def get_all(self):
        return dict(self.__productions)

    def __getitem__(self, key):
        for k, v in self.__productions:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found in productions.")

    def __setitem__(self, key, value):
        # If the key already exists, update its value
        for i, (k, v) in enumerate(self.__productions):
            if k == key:
                self.__productions[i] = (key, value)
                break
        else:
            # If the key doesn't exist, add a new production
            self.__productions.append((key, value))

    def keys(self):
        return [k for k, v in self.__productions]

    def __str__(self):
        prod_str = ""

        for key, values in self.__productions:
            prod_str += "".join(str(k) for k in key) + " -> "
            prod_str += " | ".join("".join(str(v1) for v1 in v) for v in values)
            prod_str += "\n"

        return prod_str[:-1]

if __name__ == '__main__':
    productions = ProductionSet()
    productions['S'] = [['a', 'A'], ['b', 'B']]
    productions['A'] = [['c'], ['d']]
    productions['B'] = [['e'], ['f']]

    print(productions)
    print("All Productions:", productions.get_all())
    print("Production for 'S':", productions['S'])
    print("Keys:", productions.keys())
