#!/usr/bin/env python3

import time

from enum import Enum
from typing import Sequence, List

import click

from sequence_receiver import (SequenceReceiverInterface,
                               MouseSequenceReceiver, KeyboardSequenceReceiver)
from morse_decoder import (MorseDecoder, MorseEvent, Dot, Dash)


class EventSenderInterface:
    def __init__(self):
        pass

    def send(self, data: str):
        raise NotImplementedError


class StdoutEventSender(EventSenderInterface):
    def __init__(self):
        super().__init__()

    def send(self, data: str):
        print(data, sep='', end='', flush=True)


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
    timeout_char_sec = 0.300
    keyboard_receiver = KeyboardSequenceReceiver(timeout_char_sec)
    stdout_sender = StdoutEventSender()
    main(keyboard_receiver, stdout_sender, dot, dash)


@click.command()
@click.option('--dot', default='left', help='dot input, "left" or "right"')
@click.option('--dash', default='right', help='dash input, "left" or "right"')
def clickit(dot, dash):
    timeout_char_sec = 0.300
    mouse_receiver = MouseSequenceReceiver(timeout_char_sec)
    stdout_sender = StdoutEventSender()
    main(mouse_receiver, stdout_sender, dot, dash)


if __name__ == '__main__':
    cli.add_command(typeit)
    cli.add_command(clickit)
    cli()