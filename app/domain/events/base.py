from dataclasses import dataclass, field
from abc import ABC
from uuid import uuid4


@dataclass
class BaseEvent(ABC):
    event_id: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
