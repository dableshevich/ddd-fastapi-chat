from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Слишком длинное название "{self.text[:255]}..."'


@dataclass(eq=False)
class EmptyTextError(ApplicationException):
    @property
    def message(self):
        return 'Сообщение не может быть пустым.'
