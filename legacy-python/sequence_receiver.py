import time

from abc import ABC, abstractmethod
from typing import Sequence, List, Optional, Tuple

from pynput import mouse
from pynput import keyboard


class SequenceReceiverInterface(ABC):
    """
    Get events from an input mechanism.

    Attributes
    ----------
    timeout_sec
        Timeout (in seconds) after an input that signifies the end of a sequence
    """

    def __init__(self, timeout_sec: int) -> None:
        self._timeout_sec = timeout_sec

    @property
    def timeout_sec(self) -> int:
        return self._timeout_sec

    @abstractmethod
    def receive(self) -> Sequence[str]:
        """
        Receive a sequence of input events.

        Blocks until timeout_sec has elapsed after an input event, at which 
        point the sequence of events from the start (or previous timeout) is 
        returned.

        Returns
        -------
        Sequence of input characters
        """
        raise NotImplementedError

    @abstractmethod
    def start(self) -> None:
        """
        Start listening for input events
        """
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """
        Stop listening for input events
        """
        raise NotImplementedError


class KeyboardReceiver(SequenceReceiverInterface):
    """
    Get events from keyboard input.
    """

    def __init__(self, timeout_sec: int) -> None:
        self._seq: List[str] = []
        self._input_time: Optional[float] = None
        self._listener: Optional[keyboard.Listener] = None
        super().__init__(timeout_sec)

    def _on_press(self, key: keyboard.Key) -> None:
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

    def start(self) -> None:
        if not self._listener:
            self._listener = keyboard.Listener(
                on_press=self._on_press, suppress=True)
            self._listener.start()
            self._listener.wait()

    def stop(self) -> None:
        if self._listener:
            self._listener.stop()
            self._listener = None


class MouseReceiver(SequenceReceiverInterface):
    """
    Get events from left and right mouse button clicks
    """
    LEFT = 'l'
    RIGHT = 'r'

    def __init__(self, timeout_sec: int) -> None:
        self._seq: List[str] = []
        self._input_time: Optional[float] = None
        self._listener: Optional[mouse.Listener] = None
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

    def start(self) -> None:
        if not self._listener:
            self._listener = mouse.Listener(
                on_click=self._on_click, suppress=True)
            self._listener.start()
            self._listener.wait()

    def stop(self) -> None:
        if self._listener:
            self._listener.stop()
            self._listener = None
