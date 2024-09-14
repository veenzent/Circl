import datetime
import enum
import uuid
from pydantic import BaseModel


class User(BaseModel):
    id: uuid
    username: str
    email: str
    password_hash: str
    created_at: datetime
    updated_at: datetime

class Friend(User):
    user_id: uuid
    friend_id: uuid
    status: enum(pending, accepted, rejected)
    created_at: datetime

class Message:
    id: uuid
    sender_id: uuid
    content: str
    type: enum(text, image, file)
    created_at: datetime

class Chat:
    id: uuid
    type: enum(one_on_one, group)
    created_at: datetime
    updated_at: datetime

class Group:
    id: uuid
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

class GroupMember:
    pass

class MessageRecipient:
    pass

class ChatRecipient:
    pass

class Notification:
    id: uuid
    user_id: uuid
    type: enum(message, friend_request, group_invite, ...)
    message: str
    read: bool
    created_at: datetime

