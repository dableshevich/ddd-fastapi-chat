from dataclasses import dataclass

from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.messages import ChatWithThisTitleAlreadyExists
from domain.values.messages import Title
from domain.entities.messages import Chat
from infra.repositories.messages import MemoryChatRepository


@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str


@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]):
    chat_repository: MemoryChatRepository

    async def handle(self, command: CreateChatCommand):
        if await self.chat_repository.check_chat_exists_by_title(command.title):
            raise ChatWithThisTitleAlreadyExists(command.title)

        title = Title(value=command.title)
        # TODO: считать ивенты

        new_chat = Chat.create_chat(title=title)

        await self.chat_repository.add_chat(new_chat)

        return new_chat
