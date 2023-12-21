# Finite Automaton Class

A Python class representing a deterministic finite automaton (DFA) with methods for reading specifications from a file and checking if a sequence is accepted.

## Attributes

- **input_file**: Path to the file containing automaton specifications.
- **all_states**: List of all states.
- **input_symbols**: List of input symbols.
- **initial_state**: Initial state of the automaton.
- **final_states**: List of final states.
- **transition_function**: Dictionary representing the transition function.

## Methods

### `read_from_file(input_file)`

Reads automaton specifications from the specified file.

### `seq_is_accepted(seq)`

Checks if the given sequence is accepted by the DFA.

## Example Usage

```python
dfa = FiniteAutomaton()
dfa.read_from_file("automaton.txt")

sequence = "010101"
if dfa.seq_is_accepted(sequence):
    print(f"Sequence '{sequence}' is accepted.")
else:
    print(f"Sequence '{sequence}' is not accepted."


```

## Syntax of the input files
```
input_file          = states, symbols, initial_state, final_states, transition_function
letter              = "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"
digit               = "0" | "1" | ... | "9"

states              = state, { ",", state }
state               = letter | digit

symbols             = symbol, { ",", symbol }
symbol              = letter | digit

initial_state       = state

final_states        = state, { ",", state }

transition_function = transition, { "\n", transition }
transition          = "(", state, ",", symbol, ")", "=", state

```