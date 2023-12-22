from grammar import Grammar

if __name__ == "__main__":
    grammar = Grammar("g2.txt")

    print(f"File: {grammar.get_input_file()}")
    print(f"Nonterminals: {grammar.get_nonterminals()}")
    print(f"Terminals: {grammar.get_terminals()}")
    print(f"Input: {grammar.get_input_symbol()}")
    print(f"Production set: {grammar.get_productions()}")
    print(f"CFG: {grammar.get_is_cfg()}")