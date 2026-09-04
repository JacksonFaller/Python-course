from exercises.module10.repository import InMemoryUserRepository, User, display_user


def test_repository_and_protocol_behavior():
    repo = InMemoryUserRepository([User(1, "Ada")])
    assert display_user(repo, 1) == "Ada"
    assert display_user(repo, 999) == "Unknown user"
