#!/usr/bin/env python3

import time

from enum import Enum
from typing import Sequence, List

import click

from sequence_receiver import (SequenceReceiverInterface, MouseSequenceReceiver, KeyboardSequenceReceiver)
from morse_decoder import MorseDecoder, MorseEvent

class EventSenderInterface:
    def __init__(self):
        pass

    def send(self, data: str):
        raise NotImplementedError


class StdoutEventSender(EventSenderInterface):
    def __init__(self):
        super().__init__()
    
    def send(self, data: str):
        # TODO: implement print to stdout
        pass


def main(receiver: SequenceReceiverInterface, dot: str, dash: str):
    print('Morse code decoder')
    decoder = MorseDecoder()
    
    # TODO: loop: receive, on timeout - decode, send to output
    while True:
        seq = receiver.receive()
        seq_morse = []
        for s in seq:
            if s == dot:
                seq_morse.append(MorseEvent.DOT)
            elif s == dash:
                seq_morse.append(MorseEvent.DASH)
        output = decoder.decode(seq_morse)
        print(output)


@click.group()
def cli():
    pass


@click.command()
@click.option('--dot', default='j', help='dot input')
@click.option('--dash', default='k', help='dash input')
def typeit(dot, dash):
    timeout_char_sec = 0.300
    keyboard_receiver = KeyboardSequenceReceiver(timeout_char_sec)
    main(keyboard_receiver, dot, dash)


@click.command()
@click.option('--dot', default='left', help='dot input')
@click.option('--dash', default='right', help='dash input')
def clickit(dot, dash):
    timeout_char_sec = 0.300
    mouse_receiver = MouseSequenceReceiver(timeout_char_sec)
    main(mouse_receiver, dot, dash)


if __name__ == '__main__':
    cli.add_command(typeit)
    cli.add_command(clickit)
    cli()