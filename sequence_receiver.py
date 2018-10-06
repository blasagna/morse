#!/usr/bin/env python3

import time

from enum import Enum
from typing import Sequence, List

from pynput import mouse
from pynput import keyboard

class MorseEvent(Enum):
    DOT = 1
    DASH = 2

class MorseSequence:
    def __init__(self, seq: Sequence[MorseEvent], output: str):
        self._output = output
        self._seq = seq
    
    @property
    def output(self):
        return self._output
    
    @property
    def seq(self):
        return self._seq


class SequenceReceiverInterface:
    def __init__(self, timeout_sec: int):
        self._timeout_sec = timeout_sec

    @property
    def timeout_sec(self) -> int:
        return self._timeout_sec

    def receive(self) -> str:
        raise NotImplementedError

    

class KeyboardSequenceReceiver(SequenceReceiverInterface):
    def __init__(self, timeout_sec: int):
        self._seq: List[str] = []
        self._input_time: float = None
        self._listener = keyboard.Listener(on_press=self._on_press)
        self._listener.start()
        self._listener.wait()
        super().__init__(timeout_sec)

    def _on_press(self, key):
        self._input_time = time.time()
        self._seq.append(key.char)

    def receive(self) -> Sequence[str]:
        while True:
            if self._input_time is not None:
                elapsed = time.time() - self._input_time
                if elapsed > self._timeout_sec:
                    break
        seq = self._seq[:]
        self._seq.clear()
        self._input_time = None
        return seq


class MouseSequenceReceiver(SequenceReceiverInterface):
    def __init__(self, timeout_sec: int):
        super().__init__(timeout_sec)

    def receive(self) -> str:
        # TODO: read from mouse using pyinput
        pass
