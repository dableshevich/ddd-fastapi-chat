from abc import ABC
from dataclasses import dataclass
from typing import TypeVar, Generic, Any

from domain.events.base import BaseEvent


ET = TypeVar(name='ET', bound=BaseEvent)
ER = TypeVar(name='ER', bound=Any)


@dataclass(frozen=True)
class EventHandler(ABC, Generic[ET, ER]):
    def handle(self, event: ET) -> ER:
        ...
