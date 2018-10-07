# morse
Morse code typing using separate inputs for dot and dash

One of the difficulties in learning, using, and implementing Morse code is that there are several timing specifications: dot duration, dash duration, and pause durations between elements, characters, and words. Using two distinct inputs for dot and dash decreases the number of timing specifications and makes it easier to learn and use Morse code for text entry.

# usage
```
python run.py --help
Usage: run.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  clickit
  typeit

python run.py clickit --help
Usage: run.py clickit [OPTIONS]

Options:
  --dot TEXT   dot input, "left" or "right"
  --dash TEXT  dash input, "left" or "right"
  --help       Show this message and exit.

python run.py typeit --help
Usage: run.py typeit [OPTIONS]

Options:
  --dot TEXT   dot input
  --dash TEXT  dash input
  --help       Show this message and exit.
```

# learning Morse code

There are a lot of resources out there for learning Morse code, but one good one is [Hello Morse](https://experiments.withgoogle.com/collection/morse).

Extensions to Morse code are included for:
* space     dot-dot-dash-dash
* backspace dash-dash-dash-dash