from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class ChatWithThisTitleAlreadyExists(LogicException):
    command_title: str

    @property
    def message(self):
        return f'Чат с таким названием уже существует: {self.command_title}'
