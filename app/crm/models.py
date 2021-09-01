from dataclasses import dataclass
from uuid import UUID
import uuid

@dataclass
class User:
    id_: UUID
    email: str