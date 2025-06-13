from logic.mediator import Mediator
from logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
from infra.repositories.messages import BaseChatRepository


def init_mediator(
    mediator: Mediator,
    chat_repository: BaseChatRepository
):
    mediator.register_command(
        CreateChatCommand,
        [CreateChatCommandHandler(chat_repository=chat_repository)],
    )
