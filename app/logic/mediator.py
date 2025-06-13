from dataclasses import dataclass, field
from collections import defaultdict
from collections.abc import Iterable

from domain.events.base import BaseEvent
from logic.commands.base import BaseCommand
from logic.events.base import EventHandler, ET, ER
from logic.commands.base import CommandHandler, CT, CR
from logic.exceptions.mediator import EventHandlerNotRegistered


@dataclass(eq=False)
class Mediator:
    event_map: dict[ET, list[EventHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )
    command_map: dict[CT, list[CommandHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_event(self, event: ET,
                       event_handlers: Iterable[EventHandler[ET, ER]]):
        self.event_map[event.__class__].append(event_handlers)

    def register_command(self, command: CT,
                         command_handlers: Iterable[CommandHandler[CT, CR]]):
        self.command_map[command.__class__].extend(command_handlers)

    async def handle_event(self, event: BaseEvent) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.event_map.get(event_type)

        if not handlers:
            raise EventHandlerNotRegistered(event_type)

        return [await handler.handle(event) for handler in handlers]

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.command_map.get(command_type)

        if not handlers:
            raise EventHandlerNotRegistered(command_type)

        return [await handler.handle(command) for handler in handlers]
