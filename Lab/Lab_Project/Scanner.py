from SymbolTable import SymbolTable
from PIF import Pif
from FA import FiniteAutomaton
import re


class Scanner:
    def __init__(self) -> None:
        """
        Initializes a Scanner object with a SymbolTable, PIF, and sets up token-related attributes.
        """
        self.st = SymbolTable()
        self.pif = Pif()
        self.tokens = self.__read_tokens()
        self.operators = ['%', '+', '-', '*', '/', '==', '<', '<=', '>', '>=', '=', '&&', '||']
        self.separators = ['{', '}', '(', ')', ';', '"', ',', '[', ']']
        self.reserved_words = ['if', 'else', 'print', 'read', 'while', 'int', 'str', 'bool', 'false', 'true', 'break', 'continue']
        # self.__identifier_regex = r'\b[a-zA-Z][a-zA-Z0-9]*\b'
        # self.__constant_regex = r'\b[-+]?[1-9][0-9]*\b|\b0\b'
        self.__identifier_regex = FiniteAutomaton()
        self.__constant_regex = FiniteAutomaton()
        self.__identifier_regex.read_from_file("identifier.in")
        self.__constant_regex.read_from_file("constant.in")

    
    def __flush(self) -> None:
        self.st = SymbolTable()
        self.pif = Pif()

    def _is_identifier(self, token):
        """
        Checks if a given token is an identifier.

        Parameters:
        token (str): The token to be checked.

        Returns:
        bool: True if the token is an identifier, False otherwise.
        """
        return self.__identifier_regex.seq_is_accepted(token)
        # return bool(re.match(self.__identifier_regex, token))

    def _is_constant(self, token):
        """
        Checks if a given token is a constant.

        Parameters:
        token (str): The token to be checked.

        Returns:
        bool: True if the token is a constant, False otherwise.
        """
        return self.__constant_regex.seq_is_accepted(token)
        # return bool(re.match(self.__constant_regex, token))

    def __read_tokens(self, file_path="token.in"):
        """
        Reads tokens from a file and stores them in a list.

        Parameters:
        file_path (str): Path to the input file containing tokens.

        Returns:
        list: List of tokens read from the file.
        """
        tokens = []
        with open(file_path, 'r') as file:
            for line in file:
                # Remove leading and trailing whitespaces, then split the line into tokens
                line_tokens = line.strip().split()
                # Add tokens to the list
                tokens.extend(line_tokens)
        return tokens

    def __read_file_content(self, file_path):
        """
        Reads the content of a file.

        Parameters:
        file_path (str): Path to the input file.

        Returns:
        str: Content of the file.
        """
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content

    def scan_file(self, file_path, print_tokens=False):
        """
        Scans a file and processes its tokens, updating the PIF and SymbolTable.

        Parameters:
        file_path (str): Path to the input file.
        print_tokens (bool): If True, prints the categorized tokens.

        Returns:
        None
        """
        self.__flush()
        content_string = self.__read_file_content(file_path)
        tokens = self.__get_tokens(content_string=content_string)
        if print_tokens:
            for token in tokens:
                if token in self.reserved_words:
                    print(f"{token} -> reserved word")
                elif token in self.operators:
                    print(f"{token} -> operator")
                elif token in self.separators:
                    print(f"{token} -> separator")
                elif self._is_identifier(token):
                    print(f"{token} -> identifier")
                elif self._is_constant(token):
                    print(f"{token} -> constant")
                else:
                    print(f"{token} -> error")

        nr_errors = 0

        for token in tokens:
            if token in self.reserved_words or token in self.operators or token in self.separators:
                self.pif.add(token, -1)
            elif self._is_constant(token):
                index = self.st.insert(token)
                self.pif.add("const", index)
            elif self._is_identifier(token):
                index = self.st.insert(token)
                self.pif.add("id", index)
            else:
                print(f"Lexical Error at {token}")
                nr_errors += 1

        output_file = f"{file_path}_output.txt"
        with open(output_file, 'w') as output_file:
            output_file.write("Program Internal Form (PIF):\n")
            for token, pos in self.pif.get_all():
                output_file.write(f"{token} -> {pos}\n")

            output_file.write("\nSymbol Table (SymTable):\n")
            for i, element in enumerate(self.st.hashTable.table):
                if element:
                    for pos, value in enumerate(element):
                        output_file.write(f"Index {i}, Position {pos} -> {value}\n")

        if nr_errors == 0:
            print(f"Program at path: {file_path} is correct")
        else:
            print(f"Program at path: {file_path} is incorrect")

    def __get_tokens(self, content_string):
        """
        Processes the content string and returns a list of tokens.

        Parameters:
        content_string (str): The content string to be processed.

        Returns:
        list: List of tokens.
        """
        for operator in self.operators:
            if operator == '>' or operator == '<' or operator == '=':
                continue
            content_string = content_string.replace(operator, f' {operator} ')
        pattern = r'([' + re.escape(''.join(self.separators)) + r'])'
        output_string = re.sub(pattern, r' \1 ', content_string)

        pattern = r'(?<![<>=])=(?![<>=])'
        output_string = re.sub(pattern, ' = ', output_string)

        pattern = r'(?<![<>=])<(?![<>=])'
        output_string = re.sub(pattern, ' < ', output_string)

        pattern = r'(?<![<>=])>(?![<>=])'
        output_string = re.sub(pattern, ' > ', output_string)

        tokens = output_string.split('\n')
        tokens_string = ''.join(' ' + tok + '' for tok in tokens)
        tokens = tokens_string.split(' ')
        return [token for token in tokens if len(token.strip()) > 0]


if __name__ == "__main__":
    scanner = Scanner()
    filenames = ["p1.rps", "p2.rps", "p3.rps", "p1err.rps"]
    # filenames = ["p3.rps"]
    for filename in filenames:
        scanner.scan_file(filename, print_tokens=False)
