from FA import FiniteAutomaton
import os

def show_menu():
    print("0 - Exit")
    print("1 - Read content from file")
    print("2 - Show FA content")
    print("3 - Test if sequence is accepted by the DFA")
    print("4 - Exit")

def show_fa_content(fa):
    print(f"Set of input symbols: {fa.input_symbols}")
    print(f"Set of all states: {fa.all_states}")
    print(f"Initial state: {fa.initial_state}")
    print(f"Set of final states: {fa.final_states}")
    print(f"Transition function: {fa.transition_function}")

def main():
    fa = FiniteAutomaton()

    menu_option = None

    while menu_option != 0:
        show_menu()
        menu_option = int(input(">>> "))
        os.system('clear')

        if menu_option == 1:
            print("Enter the input file name")
            file_name = input(">> ")
            os.system('clear')

            fa.read_from_file(file_name)

        if menu_option == 2:
            show_fa_content(fa)

            input("\nPress Enter to continue...")
            os.system('clear')

        if menu_option == 3:
            print("Enter the input sequence")
            seq = input(">> ")
            os.system('clear')

            result = fa.seq_is_accepted(seq)

            if result:
                print(f"The input sequence ({seq}) is accepted by the DFA")
            else:
                print(f"The input sequence ({seq}) is NOT accepted by the DFA")

            input("\nPress Enter to continue...")
            os.system('clear')
        
        if menu_option == 4:
            exit()

if __name__ == "__main__":
    main()
