from abc import (ABC, abstractmethod)
from pynput.keyboard import Controller


class EventSenderInterface(ABC):
    """
    Send events to an output mechanism.
    """

    @abstractmethod
    def send(self, data: str) -> None:
        """
        Send data to output.

        Parameters
        ----------
        data
            Output character data
        """
        raise NotImplementedError


class StdoutSender(EventSenderInterface):
    """
    Send events to stdout in the console.
    """

    def __init__(self) -> None:
        super().__init__()

    def send(self, data: str) -> None:
        print(data, sep='', end='', flush=True)


class KeyboardSender(EventSenderInterface):
    """
    Send events as keyboard output.
    """

    def __init__(self) -> None:
        self._keyboard = Controller()

    def send(self, data: str) -> None:
        try:
            self._keyboard.type(data)
        except Controller.InvalidCharacterException:
            print('untypeable data {}'.format(data))
