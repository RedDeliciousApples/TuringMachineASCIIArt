## What's this?

A simple Python script which simulates a [Turing machine](https://en.wikipedia.org/wiki/Turing_machine), and provides some nice* ASCII art to show the state of the machine. This project was built so I could get some experience making a Turing machine. Hopefully you'll find it useful.

*I think the art is nice. Hopefully you do too.

## Usage
See that big comment block on line 93? The one that looks like this?
```
#########################################################################################################################
###################### YOU MAY SAFELY EDIT VARIABLES AND FUNCTION ARGUMENTS BELOW THIS BLOCK ############################
#########################################################################################################################
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
```

You can edit any of the variables there, provided that:

- ```states``` must be a dictionary, with a tuple of size 2 as the key, and a tuple of size 3 as the value.
- ```initial_tape``` must be a List of the numbers 0 or 1.
- ```TuringMachine``` takes in the ```initial_tape```, a ```state``` (first value of the key tuple),```states```, and a desired ```state``` which the machine should halt at.

Enjoy!


