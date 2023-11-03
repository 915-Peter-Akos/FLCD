from SymbolTable import SymbolTable
from PIF import Pif
import re


class Scanner:
    def __init__(self) -> None:
        self.st = SymbolTable()
        self.__pif = Pif()
        self.tokens = self.__read_tokens()
        self.operators = ['+', '-', '*', '/', '==', '<', '<=', '>', '>=', '=', '&&', '||']
        self.separators = ['{', '}', '(', ')', ';', '"', ',']
        self.reserved_words = ['if', 'else', 'print', 'read', 'while', 'int', 'str']
        self.__identifier_regex = r'\b[a-zA-Z][a-zA-Z0-9]*\b'
        self.__constant_regex = r'\b[-+]?[1-9][0-9]*\b|\b0\b'


    def _is_identifier(self, token):
        return bool(re.match(self.__identifier_regex, token))

    def _is_constant(self, token):
        return bool(re.match(self.__constant_regex, token))
        
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
         with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    
    def scan_file(self, file_path, print_tokens=False):
        content_string = self.__read_file_content(file_path)
        tokens = self.get_tokens(content_string=content_string)
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

        for token in tokens:
            if token in self.reserved_words or token in self.operators or token in self.separators:
                self.__pif.add(token, -1)
            elif self._is_constant(token):
                index = self.st.insert(token)
                self.__pif.add("const", index)
            elif self._is_identifier(token):
                index = self.st.insert(token)
                self.__pif.add("id", index)
            else:
                print(f"Lexical Error at {token}")
        
        print("Program is correct")



        

    def get_tokens(self, content_string):
        pattern = r'([' + re.escape(''.join(self.separators)) + r'])' # '([\\{\\}\\(\\);",])'
        output_string_1 = re.sub(pattern, r' \1 ', content_string)

        pattern = r'(?<![<>=])=(?![<>=])'
        output_string = re.sub(pattern, ' = ', output_string_1)

        tokens = output_string.split('\n')
        tokens_string = ''.join(' ' + tok + '' for tok in tokens)
        tokens = tokens_string.split(' ')
        return [token for token in tokens if len(token.strip()) > 0]

        

    
if __name__ == "__main__":
    scanner = Scanner()
    # filenames = ["p1.rps", "p2.rps", "p3.rps", "p1err.rps"]
    filenames = ["p1.rps"]
    for filename in filenames:
        scanner.scan_file(filename)


    
