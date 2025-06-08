import pytest
from datetime import datetime

from domain.values.messages import Text, Title
from domain.entities.messages import Message, Chat
from domain.exceptions.messages import TitleTooLongException


def test_create_message_success():
    text = Text('Hello')
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_chat_success():
    title = Title('title')
    chat = Chat(title=title)

    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date() == datetime.today().date()


def test_create_chat_too_long():
    with pytest.raises(TitleTooLongException):
        title = Title('a' * 400)


def test_add_chat_to_message():
    title = Title('title')
    chat = Chat(title=title)

    text = Text('Hello')
    message = Message(text=text)

    chat.add_message(message=message)

    assert message in chat.messages

def test_message_new_event():
    text = Text('Hello')
    message = Message(text=text)

    title = Title('title')
    chat = Chat(title=title)

    chat.add_message(message=message)
    events = chat.pull_events()
    pulled_events = chat.pull_events()

    assert not pulled_events, pulled_events
    assert len(events) == 1, events

    new_event = events[0]

    assert new_event.message_text == message.text.as_generic_type()
    assert new_event.message_oid == message.oid
    assert new_event.chat_oid == chat.oid
