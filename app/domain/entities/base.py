from dataclasses import dataclass, field
from abc import ABC
from datetime import datetime
from uuid import uuid4
from copy import copy

from domain.events.base import BaseEvent


@dataclass
class BaseEntity(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    _events: list[BaseEvent] = field(
        default_factory=list,
        kw_only=True,
    )

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return __value.oid == self.oid

    def __hash__(self) -> int:
        return hash(self.oid)

    def register_event(self, event: BaseEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> list[BaseEvent]:
        registered_events = copy(self._events)
        self._events.clear()

        return registered_events
