from typing import *


class TuringMachine:
    def __init__(self, tape: List[int], initial_state: str, state_machine: Dict[Tuple[str, int], Tuple[str, int, str]],
                 pos: int, end_state: str):
        self.tape = tape
        self.state = initial_state
        self.state_table = state_machine
        self.pos = pos
        self.end_state = end_state

    def greet(self):
        return (f"Starting with tape: {self.tape}\n and state {self.state}\n with state table \n {self.state_table}\n"
                f" at index {self.pos}\n to reach state {self.end_state}.\n")

    def step(self) -> bool:

        current_symbol = self.tape[self.pos]

        if (self.state, current_symbol) in self.state_table:

            old_state = self.state

            new_state, new_symbol, move = self.state_table[(self.state, current_symbol)]
            self.tape[self.pos] = new_symbol

            if move == 'Right':
                self.pos += 1
            elif move == 'Left':
                self.pos -= 1

            self.state = new_state
            print(f"The symbol {current_symbol} at index {self.pos - 1} was updated to a new symbol: {new_symbol}. The machine swicthed from state {old_state} to {new_state}. The tape head moved {move.lower()}.")

            art(self.tape, self.pos)

            return True
        else:
            return False

    def run(self):
        while self.state != self.end_state and self.step():
            pass

        if self.state == self.end_state:
            print(f"Halted because desired state of {self.end_state} was reached.")
        else:
            print(f"Halted due to unknown state of {self.state}.")


def art(tape: List[int], pos: int):
    tape_length = len(tape)

    print("-" * (tape_length * 11))

    # Note: there are 5 spaces

    print("     |     |" * (tape_length - 1))

    for i in range(1, tape_length):
        print(f"     |  {tape[i]}  |", end="")

    # empty print statement for 1 newline
    print("")

    print("     |     |" * (tape_length - 1))

    print("-" * (tape_length * 11))

    arrow(pos)


def arrow(pos: int):
    # number of spaces on left: 8, 6, 4, 6, 6, 6
    # for simplicity, we use an offset of 6 spaces
    # 12 spaces between centers of each cell
    offset: str = "      " + ((" " * 12) * pos)

    # This adds 2 spaces
    print(f"{offset + '  '}.   ")
    print(f"{offset}.:;:. ")
    # This removes last 2 characters
    print(f"{offset[:-2]}.:;;;;;:.   ")
    print(f"{offset};;;;;   ")
    print(f"{offset};;;;;   ")
    print(f"{offset};;;;;")


# Format: If at (state, symbol), do (new_state, new_symbol, move)
# Our symbols are ints, but could be anything
states = {
    ('s0', 1): ('s0', 0, 'Right'),
    ('s0', 0): ('s1', 1, 'Right'),
    ('s2', 0): ('s1', 1, 'Right'),
    ('s1', 0): ('s0', 1, 'Right'),
    ('s1', 1): ('s1', 0, 'Right'),
}

initial_tape = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

if __name__ == "__main__":
    machine = TuringMachine(initial_tape, 's2', states, 0, "s1")
    print(machine.greet())
    machine.run()
