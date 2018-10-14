# morse
Morse code typing using separate inputs for dot and dash

One of the difficulties in learning and using Morse code is that there are several timing specifications: dot duration, dash duration, and pause durations between elements, characters, and words. Using two distinct inputs for dot and dash decreases the number of timing specifications and makes it easier to learn and use Morse code for text entry.

## usage
```
Usage: run.py [OPTIONS]

Options:
  --dot TEXT                  dot input (use l or r for mouse buttons)
                              [default: j]
  --dash TEXT                 dash input (use l or r for mouse buttons)
                              [default: k]
  --enter [keyboard|mouse]    input method  [default: keyboard]
  --output [keyboard|stdout]  output method  [default: keyboard]
  --timeout FLOAT             end of character timeout (sec)  [default: 0.2]
  --help                      Show this message and exit.
```

## learning Morse code

There are many resources out there for learning Morse code, but one good one is [Hello Morse](https://experiments.withgoogle.com/collection/morse).

Extensions to Morse code are included for:
* space     dot-dot-dash-dash
* backspace dash-dash-dash-dash

# run tests
TODO: add unit tests