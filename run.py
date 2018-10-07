#!/usr/bin/env python3

# TODO: add docstrings for files, modules, classes
import time

from enum import Enum
from typing import Sequence, List

import click

from sequence_receiver import (SequenceReceiverInterface, MouseReceiver,
                               KeyboardReceiver)
from morse_decoder import (MorseDecoder, MorseEvent, Dot, Dash)
from event_sender import (EventSenderInterface, StdoutSender, KeyboardSender)


def main(receiver: SequenceReceiverInterface, sender: EventSenderInterface,
         dot: str, dash: str):
    print('Morse code decoder')
    decoder = MorseDecoder()

    while True:
        seq = receiver.receive()
        # convert input sequence to dots and dashes
        seq_morse = [
            Dot if s == dot else Dash if s == dash else MorseEvent.INVALID
            for s in seq
        ]
        char = decoder.decode(seq_morse)
        sender.send(char)


@click.group()
def cli():
    pass


@click.command()
@click.option('--dot', default='j', help='dot input')
@click.option('--dash', default='k', help='dash input')
def typeit(dot, dash):
    # TODO: make timeout a runtime arg
    # TODO: validate args. dot/dash should be len 1
    timeout_char_sec = 0.300
    receiver = KeyboardReceiver(timeout_char_sec)
    sender = StdoutSender()
    main(receiver, sender, dot, dash)


@click.command()
@click.option('--dot', default='left', help='dot input, "left" or "right"')
@click.option('--dash', default='right', help='dash input, "left" or "right"')
def clickit(dot, dash):
    # TODO: validate args. dot/dash should be "left" or "right"
    timeout_char_sec = 0.300
    receiver = MouseReceiver(timeout_char_sec)
    sender = KeyboardSender()
    main(receiver, sender, dot, dash)


if __name__ == '__main__':
    cli.add_command(typeit)
    cli.add_command(clickit)
    cli()