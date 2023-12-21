class FiniteAutomaton:
    def __init__(self):
        self.input_file = ""
        self.all_states = []
        self.input_symbols = []
        self.initial_state = None
        self.final_states = []
        self.transition_function = {}

    def read_from_file(self, input_file):
        with open(input_file) as file:
            lines = [line.replace(' ', '').strip() for line in file.readlines()]
            self.all_states = lines[0].split(',')
            self.input_symbols = lines[1].split(',')
            self.initial_state = lines[2]
            self.final_states = lines[3].split(',')

            transition_function = {}
            for line in lines[4:]:
                state = line[1]
                input_symbol = line[3]
                next_state = line[6]
                transition_function[state, input_symbol] = next_state
            self.transition_function = transition_function

    def seq_is_accepted(self, seq):
        current_state = self.initial_state

        for symbol in seq:
            try:
                current_state = self.transition_function[current_state, symbol]
            except KeyError:
                return False

        return current_state in self.final_states
