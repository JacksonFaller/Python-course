from dataclasses import dataclass
from typing import Protocol


@dataclass
class User:
    id: int
    name: str


class UserRepository(Protocol):
    def get(self, user_id: int) -> User | None:
        ...


class InMemoryUserRepository:
    def __init__(self, users: list[User]) -> None:
        self._users = users

    def get(self, user_id: int) -> User | None:
        return next((user for user in self._users if user.id == user_id), None)


def display_user(repository: UserRepository, user_id: int) -> str:
    user = repository.get(user_id)
    return user.name if user is not None else "Unknown user"
