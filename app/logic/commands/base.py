from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic


@dataclass(frozen=True)
class BaseCommand(ABC):
    ...


CT = TypeVar(name='CT', bound=BaseCommand)
CR = TypeVar(name='CR', bound=Any)


@dataclass(frozen=True)
class CommandHandler(ABC, Generic[CT, CR]):
    @abstractmethod
    async def handle(self, command: CT) -> CR:
        ...
