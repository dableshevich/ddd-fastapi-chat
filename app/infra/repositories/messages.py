from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from domain.entities.messages import Chat
from domain.values.messages import Title


@dataclass
class BaseChatRepository(ABC):
    @abstractmethod
    async def check_chat_exists_by_title(self, title: str) -> bool:
        ...

    @abstractmethod
    async def add_chat(self, chat: Chat):
        ...


@dataclass
class MemoryChatRepository(ABC):
    _saved_chats: list[Chat] = field(
        default_factory=list,
        kw_only=True
    )

    async def check_chat_exists_by_title(self, title: str) -> bool:
        try:
            new_title = Title(title)
            return bool(next(
                chat for chat in self._saved_chats if chat.title == new_title
            ))
        except StopIteration:
            return False

    async def add_chat(self, chat: Chat):
        self._saved_chats.append(chat)
