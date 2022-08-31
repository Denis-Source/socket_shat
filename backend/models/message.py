from logging import getLogger

from .base_model import BaseModel
from .model_types import ModelTypes


class Message(BaseModel):
    TYPE = ModelTypes.MESSAGE
    logger = getLogger(f"{TYPE}-model")

    def __init__(self, body: str, user, room):
        super().__init__()
        self.body = body
        self.user = user
        self.room = room
        self.name = f"{self.TYPE}-{self.get_uuid()}"

        self.logger.debug(f"created {self}")

    def __str__(self):
        return self.name

    def get_dict(self) -> dict:
        self.logger.debug(f"crated dict from {self}")

        return {
            "type": self.TYPE,
            "uuid": str(self.get_uuid()),
            "body": self.body,
            "created": self.get_iso_created(),
            "user": self.user.get_dict(),
            "room": self.room.get_dict(),
            "name": self.name
        }
