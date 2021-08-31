from dataclasses import dataclass
from uuid import UUID
import uuid

@dataclass
class User:
    _id: UUID
    email: str