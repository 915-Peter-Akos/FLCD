from production_set import ProductionSet

class Grammar:

    def __init__(self, input_file):
        self.__input_file = input_file
        self.__nonterminals = list()
        self.__terminals = list()
        self.__input_symbol = None
        self.__productions = ProductionSet()
        self.__is_cfg = None

        self.__read_from_file()
        self.__is_cfg = self.__check_if_cfg()

    def get_input_file(self):
        return self.__input_file
    
    def get_nonterminals(self):
        return self.__nonterminals
    
    def get_terminals(self):
        return self.__terminals
    
    def get_input_symbol(self):
        return self.__input_symbol
    
    def get_productions(self):
        return self.__productions
    
    def get_is_cfg(self):
        return self.__is_cfg

    def __read_from_file(self):
        with open(self.__input_file) as file:
            lines = file.readlines()

        self.__nonterminals = [symbol for symbol in lines[0].split()]
        self.__terminals = [symbol for symbol in lines[1].split()]
        self.__input_symbol = lines[2].strip()

        for line in lines[3:]:
            lhs, rhs = [tuple(side.strip().split(' ')) for side in line.split('->')]

            if lhs not in self.__productions.get_all():
                self.__productions[lhs] = list()
            self.__productions[lhs].append(rhs)

    def __check_if_cfg(self):
        return all(len(key) == 1 for key in self.__productions.keys())