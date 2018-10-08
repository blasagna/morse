#!/usr/bin/env python3

# TODO: add docstrings for files, modules, classes
import time
import sys

from enum import Enum
from typing import Sequence, List, Optional

import click

from sequence_receiver import (SequenceReceiverInterface, MouseReceiver,
                               KeyboardReceiver)
from morse_decoder import (MorseDecoder, MorseEvent, Dot, Dash)
from event_sender import (EventSenderInterface, StdoutSender, KeyboardSender)


def main(receiver: SequenceReceiverInterface, sender: EventSenderInterface,
         dot: str, dash: str):
    print('Morse code decoder.')
    print('Enter an invalid input to exit:')
    print('  keyboard: any key other than dot/dash')
    print('  mouse: ctrl-c')
    decoder = MorseDecoder()

    running: bool = True
    while running:
        receiver.start()
        seq = receiver.receive()
        receiver.stop()

        # convert input sequence to dots and dashes
        seq_morse = [
            Dot if s == dot else Dash if s == dash else MorseEvent.INVALID
            for s in seq
        ]
        if MorseEvent.INVALID in seq_morse:
            running = False
        else:
            char = decoder.decode(seq_morse)
            sender.send(char)
    print('Goodbye.')


@click.command()
@click.option(
    '--dot',
    default='j',
    help='dot input (use l or r for mouse buttons)',
    show_default=True)
@click.option(
    '--dash',
    default='k',
    help='dash input (use l or r for mouse buttons)',
    show_default=True)
@click.option(
    '--enter',
    type=click.Choice(['keyboard', 'mouse']),
    default='keyboard',
    help='input method',
    show_default=True)
@click.option(
    '--output',
    type=click.Choice(['keyboard', 'stdout']),
    default='keyboard',
    help='output method',
    show_default=True)
@click.option(
    '--timeout',
    default=0.200,
    help='end of character timeout (sec)',
    show_default=True)
def cli(dot, dash, enter, output, timeout):
    enter: str = enter.lower()
    output: str = output.lower()
    dot: str = dot.lower()
    dash: str = dash.lower()

    receiver: Optional[SequenceReceiverInterface] = None
    sender: Optional[EventSenderInterface] = None

    if enter == 'keyboard':
        assert len(dot) == 1
        assert len(dash) == 1
        receiver = KeyboardReceiver(timeout)
    elif enter == 'mouse':
        assert dot in ('l', 'r')
        assert dash in ('l', 'r')
        receiver = MouseReceiver(timeout)
    else:
        print('Invalid input method:', enter)
        sys.exit(1)

    if output == 'keyboard':
        sender = KeyboardSender()
    elif output == 'stdout':
        sender = StdoutSender()
    else:
        print('Invalid output method:', output)
        sys.exit(1)

    assert receiver
    assert sender
    main(receiver, sender, dot, dash)


if __name__ == '__main__':
    cli()
