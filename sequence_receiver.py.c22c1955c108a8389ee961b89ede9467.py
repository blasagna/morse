import time

from abc import ABC, abstractmethod
from typing import Sequence, List, Optional

from pynput import mouse
from pynput import keyboard


class SequenceReceiverInterface(ABC):
    def __init__(self, timeout_sec: int) -> None:
        self._timeout_sec = timeout_sec

    @property
    def timeout_sec(self) -> int:
        return self._timeout_sec

    @abstractmethod
    def receive(self) -> Sequence[str]:
        raise NotImplementedError


class KeyboardReceiver(SequenceReceiverInterface):
    def __init__(self, timeout_sec: int) -> None:
        self._seq: List[str] = []
        self._input_time: Optional[float] = None
        self._listener = keyboard.Listener(
            on_press=self._on_press, suppress=True)
        self._listener.start()
        self._listener.wait()
        super().__init__(timeout_sec)

    def _on_press(self, key) -> None:
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


class MouseReceiver(SequenceReceiverInterface):
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self, timeout_sec: int) -> None:
        self._seq: List[str] = []
        self._input_time: Optional[float] = None
        self._listener = mouse.Listener(on_click=self._on_click, suppress=True)
        self._listener.start()
        self._listener.wait()
        super().__init__(timeout_sec)

    def _on_click(self, x, y, button, pressed) -> None:
        self._input_time = time.time()
        if pressed and button == mouse.Button.left:
            self._seq.append(MouseReceiver.LEFT)
        elif pressed and button == mouse.Button.right:
            self._seq.append(MouseReceiver.RIGHT)

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
