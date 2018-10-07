from abc import (ABC, abstractmethod)
from pynput.keyboard import Controller


class EventSenderInterface(ABC):
    @abstractmethod
    def send(self, data: str) -> None:
        raise NotImplementedError


class StdoutSender(EventSenderInterface):
    def __init__(self) -> None:
        super().__init__()

    def send(self, data: str) -> None:
        print(data, sep='', end='', flush=True)


# TODO: debug keyboard output with keyboard input
class KeyboardSender(EventSenderInterface):
    def __init__(self) -> None:
        self._keyboard = Controller()

    def send(self, data: str) -> None:
        print('sending', data)
        try:
            self._keyboard.type(data)
        except Controller.InvalidCharacterException:
            print('untypeable data {}'.format(data))
