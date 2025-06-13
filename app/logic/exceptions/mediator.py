from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class EventHandlerNotRegistered(LogicException):
    event_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчики для события: {self.event_type}'


@dataclass(eq=False)
class CommandHandlerNotRegistered(LogicException):
    command_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчики для комманды: {self.command_type}'
