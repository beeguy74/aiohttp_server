from dataclasses import dataclass, field

from app.admin.models import Admin


@dataclass
class Database:
    # TODO: добавить поля admins и questions
    admins: list[Admin] = field(default_factory=list)

    @property
    def next_admin_id(self) -> int:
        return len(self.admins) + 1

    def clear(self):
        self.admins = []
