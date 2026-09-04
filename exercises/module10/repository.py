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

    def get(self, user_id: int):
        # TODO: add a precise return annotation and implementation.
        raise NotImplementedError


def display_user(repository: UserRepository, user_id: int) -> str:
    # TODO
    raise NotImplementedError
